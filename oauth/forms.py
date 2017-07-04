from django import forms
from .models import UserProfile


class UserProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'length': '10'}))
    about = forms.TextInput(attrs={'class': 'md-textarea', 'length': '160'})

    class Meta:
        model = UserProfile
        fields = ['year', 'phone', 'avatar', 'cover', 'hometown', 'skills', 'about']
