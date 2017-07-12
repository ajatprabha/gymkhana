from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import SocialLinkOwnerMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import UserProfile, SocialLink
from .forms import UserProfileUpdateForm, SocialLinkForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'oauth/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)
        context['social_media_count'] = len(SocialLink.SM_CHOICES)
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'oauth/profile_edit.html'
    form_class = UserProfileUpdateForm

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

