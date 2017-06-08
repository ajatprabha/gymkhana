from django.db import models
from oauth.models import UserProfile
from ckeditor_uploader.fields import RichTextUploadingField


class Topic(models.Model):
    # Choices
    CAT_CHOICES = (
        ('Q', 'Question'),
        ('F', 'Feedback'),
    )
    # Topic Database Model
    owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    category = models.CharField(max_length=3, choices=CAT_CHOICES, default='Q')
    title = models.CharField(max_length=256)
    content = RichTextUploadingField
    slug = models.SlugField(unique=True)
    views = models.PositiveIntegerField(default=0)
    answers = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    topic = models.OneToOneField(Topic, on_delete=models.CASCADE)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    content = RichTextUploadingField
    total_votes = models.SmallIntegerField(default=0)


class Vote(models.Model):
    # Choices
    VOTE_CHOICE = (
        (-1, 'Dislike'),
        (0, 'Neutral'),
        (1, 'Like'),
    )
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    value = models.SmallIntegerField(choices=VOTE_CHOICE, default=0)


class Tag(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    hits = models.PositiveIntegerField(default=1)
