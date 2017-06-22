from django.db import models
from oauth.models import UserProfile
from django.core.urlresolvers import reverse
from versatileimagefield.fields import VersatileImageField


class Society(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    cover = VersatileImageField(upload_to='society_%Y', blank=True, null=True)
    secretary = models.ForeignKey(UserProfile, related_name='secy')
    vice_secretary = models.ForeignKey(UserProfile, related_name='vice_secy')
    mentor = models.ForeignKey(UserProfile, related_name='mentor')
    slug = models.SlugField(unique=True)
    year = models.DateField()

    def get_absolute_url(self):
        return reverse('main:soc-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Club(models.Model):
    name = models.CharField(max_length=128)
    society = models.ForeignKey(Society)
    description = models.TextField()
    cover = VersatileImageField(upload_to='club_%Y', blank=True, null=True)
    captain = models.ForeignKey(UserProfile, related_name='captain')
    vice_captain_one = models.ForeignKey(UserProfile, related_name='vice_cap_one')
    vice_captain_two = models.ForeignKey(UserProfile, related_name='vice_cap_two')
    slug = models.SlugField(unique=True)
    year = models.DateField()

    def get_absolute_url(self):
        return reverse('main:club-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class SocialLink(models.Model):
    SM_CHOICES = (
        ('FB', 'Facebook'),
        ('TW', 'Twitter'),
        ('GP', 'Google Plus'),
        ('IG', 'Instagram'),
        ('GH', 'GitHub'),
        ('FK', 'Flickr'),
        ('YT', 'YouTube'),
    )

    club = models.ForeignKey(Club)
    social_media = models.CharField(max_length=2, choices=SM_CHOICES)
    link = models.URLField
    icon_class = models.CharField(max_length=32, blank=True, null=True)
    fa_icon = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.club.name + self.social_media

