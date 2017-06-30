from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserProfile
from .forms import UserProfileUpdateForm
from django.core.exceptions import PermissionDenied


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'oauth/profile_detail.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    template_name = 'oauth/profile_edit.html'
    form_class = UserProfileUpdateForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated() and request.user.id is not self.get_object().user.id:
            raise PermissionDenied
        return super(ProfileEditView, self).dispatch(request, *args, **kwargs)
