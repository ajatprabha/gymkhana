import datetime
from django.db import models
from django.core.validators import RegexValidator
from oauth.models import UserProfile
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from versatileimagefield.fields import VersatileImageField


YEAR_CHOICES = []
for r in range(2008, (datetime.datetime.now().year+2)):
    YEAR_CHOICES.append((str(r), r))


class Society(models.Model):
    # Validators
    valid_year = RegexValidator(r'^[0-9]{4}$', message='Not a valid year!')
    # Model
    name = models.CharField(max_length=128)
    description = RichTextUploadingField(blank=True)
    cover = VersatileImageField(upload_to='society_%Y', blank=True, null=True)
    secretary = models.ForeignKey(UserProfile, related_name='secy')
    vice_secretary = models.ForeignKey(UserProfile, related_name='vice_secy')
    mentor = models.ForeignKey(UserProfile, related_name='mentor')
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=False)
    year = models.CharField(max_length=4, choices=YEAR_CHOICES, validators=[valid_year])

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Societies"

    def get_absolute_url(self):
        return reverse('main:soc-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name + " - " + str(self.year)


class Club(models.Model):
    # Model
    name = models.CharField(max_length=128)
    society = models.ForeignKey(Society)
    description = RichTextUploadingField(blank=True)
    cover = VersatileImageField(upload_to='club_%Y', blank=True, null=True)
    captain = models.ForeignKey(UserProfile, related_name='captain')
    vice_captain_one = models.ForeignKey(UserProfile, related_name='vice_cap_one')
    vice_captain_two = models.ForeignKey(UserProfile, related_name='vice_cap_two')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["name"]

    @property
    def year(self):
        return self.society.year

    @property
    def is_active(self):
        return self.society.is_active

    def get_absolute_url(self):
        return reverse('main:club-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name + " - " + str(self.year)


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

