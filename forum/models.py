from django.db import models
from oauth.models import UserProfile
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.urlresolvers import reverse
from hitcount.models import HitCountMixin


class Topic(models.Model, HitCountMixin):
    # Choices
    CAT_CHOICES = (
        ('Q', 'Question'),
        ('F', 'Feedback'),
    )
    # Topic Database Model
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.CharField(max_length=3, choices=CAT_CHOICES, default='Q')
    title = models.CharField(max_length=256)
    content = RichTextUploadingField(blank=True)
    tags = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def number_of_answers(self):
        return self.answer_set.count()

    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse('forum:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Answer(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = RichTextUploadingField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def number_of_votes(self):
        return self.vote_set.count()

    def __str__(self):
        return "On: " + str(self.topic.title) + " by " + str(self.owner.user.first_name) + " " + str(self.owner.user.last_name)


class Vote(models.Model):
    # Choices
    VOTE_CHOICE = (
        (-1, 'Dislike'),
        (0, 'Neutral'),
        (1, 'Like'),
    )
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    value = models.SmallIntegerField(choices=VOTE_CHOICE, default=0)


class Tag(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    hits = models.PositiveIntegerField(default=1)
