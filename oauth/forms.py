from django import forms
from .models import UserProfile
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class UserProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'length': '10'}))
    about = forms.TextInput(attrs={'class': 'md-textarea', 'length': '512'})

    class Meta:
        model = UserProfile
        fields = ['year', 'phone', 'avatar', 'cover', 'hometown', 'skills', 'about']
