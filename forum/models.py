from django.db import models
from oauth.models import UserProfile
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.urlresolvers import reverse


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
    content = RichTextUploadingField(blank=True)
    slug = models.SlugField(unique=True)
    views = models.PositiveIntegerField(default=0)
    answers = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Answer(models.Model):
    topic = models.OneToOneField(Topic, on_delete=models.CASCADE)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
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
