from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied


class UserAuthorMixin(LoginRequiredMixin):
    """
    Checks that the user is the author of the article. If they are not, return a
    403 error
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated() and request.user is not self.get_object().author.user:
            raise PermissionDenied
        return super(UserAuthorMixin, self).dispatch(request, *args, **kwargs)
