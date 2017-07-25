from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render
from .mixins import SocialLinkOwnerMixin
from .models import UserProfile, SocialLink
from .forms import UserProfileUpdateForm, SocialLinkForm, SignUpForm

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'oauth/profile_detail.html'

    def get_object(self, queryset=None):
        roll = self.kwargs.get('roll')
        return get_object_or_404(UserProfile, roll=roll, email_confirmed=True)

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['social_media_count'] = len(SocialLink.SM_CHOICES)
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'oauth/profile_edit.html'
    form_class = UserProfileUpdateForm

    def get_object(self, queryset=None):
        roll = self.kwargs.get('roll')
        return get_object_or_404(UserProfile, roll=roll, email_confirmed=True)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated() and request.user.id is not self.get_object().user.id:
            raise PermissionDenied
        return super(ProfileEditView, self).dispatch(request, *args, **kwargs)


class SocialLinkCreateView(LoginRequiredMixin, CreateView):
    model = SocialLink
    template_name = 'oauth/sociallink_create.html'
    form_class = SocialLinkForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SocialLinkCreateView, self).form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(SocialLinkCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class SocialLinkUpdateView(SocialLinkOwnerMixin, UpdateView):
    model = SocialLink
    template_name = 'oauth/sociallink_update.html'
    form_class = SocialLinkForm

    def get_object(self, queryset=None):
        user = self.kwargs.get('username')
        social_media = self.kwargs.get('social_media')  # gets social_media value from url
        return get_object_or_404(SocialLink, user__username=user, social_media=social_media)


class SocialLinkDeleteView(SocialLinkOwnerMixin, DeleteView):
    model = SocialLink

    def get_success_url(self):
        return self.request.user.userprofile.get_absolute_url()

    def get_object(self, queryset=None):
        user = self.kwargs.get('username')
        social_media = self.kwargs.get('social_media')  # gets social_media value from url
        return get_object_or_404(SocialLink, user__username=user, social_media=social_media)


class RegisterView(CreateView):
    model = UserProfile
    template_name = 'oauth/register.html'
    success_url = '/'
    form_class = SignUpForm

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.is_active = False
    #     self.object.save()


class AccountActivationView(RedirectView):
    def get(self, request, uidb64=None, token=None, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
        activated_user = UserProfile.objects.activate_account(uidb64=uidb64, token=token)

        if activated_user:
            return redirect(activated_user.userprofile.get_absolute_url())
        else:
            # invalid link
            return render(self.request, 'oauth/invalid_activation.html')


def get_activation_link(request, roll):
    userprofile = UserProfile.objects.get(roll=roll)
    uid = urlsafe_base64_encode(force_bytes(userprofile.user.pk))
    token = account_activation_token.make_token(userprofile.user)
    return render(request, 'oauth/account_activation_email.html',
                  {'uidb64': uid, 'token': token, 'user': userprofile.user})
