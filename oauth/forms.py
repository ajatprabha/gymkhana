from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, SocialLink


class UserProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'length': '10'}))
    about = forms.TextInput(attrs={'class': 'md-textarea', 'length': '160'})

    class Meta:
        model = UserProfile
        fields = ['year', 'phone', 'avatar', 'cover', 'hometown', 'skills', 'about']


class SocialLinkForm(forms.ModelForm):

    class Meta:
        model = SocialLink
        fields = ['social_media', 'link']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        links = SocialLink.objects.filter(user=user)
        taken_choices = []
        for link in links:
            for key, value in SocialLink.SM_CHOICES:
                if link.social_media == key:
                    taken_choices += [(key, value)]
        super(SocialLinkForm, self).__init__(*args, **kwargs)
        self.fields['social_media'].choices = sorted(set(self.fields['social_media'].choices) ^ set(taken_choices))


class EmailVerifyForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        data = self.cleaned_data['email']
        if not data.endswith('@iitj.ac.in'):
            raise forms.ValidationError('Invalid Email address!')
        return data


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
