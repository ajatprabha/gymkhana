from django import forms
from .models import Topic
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TopicForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=CKEditorUploadingWidget())
    tags = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Topic
        fields = ['category', 'title', 'tags', 'content']
