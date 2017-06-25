import datetime
from django.db import models
from django.core.validators import RegexValidator
from oauth.models import UserProfile
from django.core.urlresolvers import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from versatileimagefield.fields import VersatileImageField, PPOIField
from photologue.models import Gallery

YEAR_CHOICES = []
for r in range(2008, (datetime.datetime.now().year + 2)):
    YEAR_CHOICES.append((str(r), r))


class Society(models.Model):
    # Validators
    valid_year = RegexValidator(r'^[0-9]{4}$', message='Not a valid year!')
    # Model
    name = models.CharField(max_length=128)
    description = RichTextUploadingField(blank=True)
    cover = VersatileImageField('Cover', upload_to='society_%Y', blank=True, null=True,
                                help_text="Upload high quality picture")
    secretary = models.ForeignKey(UserProfile, related_name='secy')
    vice_secretary = models.ForeignKey(UserProfile, related_name='vice_secy')
    mentor = models.ForeignKey(UserProfile, related_name='mentor')
    slug = models.SlugField(unique=True, help_text="This will be used as URL. /society/slug")
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
    # Choices
    SKIN_CHOICES = (
        ('white-skin', 'White'),
        ('black-skin', 'Black'),
        ('cyan-skin', 'Cyan'),
        ('mdb-skin', 'MDB'),
        ('deep-purple-skin', 'Deep Purple'),
        ('navy-blue-skin', 'Navy Blue'),
        ('pink-skin', 'Pink'),
        ('indigo-skin', 'Indigo'),
        ('light-blue-skin', 'Light Blue'),
        ('grey-skin', 'Grey'),
    )
    # Model
    name = models.CharField(max_length=128)
    society = models.ForeignKey(Society)
    description = RichTextUploadingField(blank=True)
    cover = VersatileImageField(upload_to='club_%Y', blank=True, null=True,
                                help_text="Upload high quality picture")
    skin = models.CharField(max_length=32, choices=SKIN_CHOICES, blank=True, null=True,
                            help_text="Choose a skin while displaying club page.")
    captain = models.ForeignKey(UserProfile, related_name='captain')
    vice_captain_one = models.ForeignKey(UserProfile, related_name='vice_cap_one')
    vice_captain_two = models.ForeignKey(UserProfile, related_name='vice_cap_two')
    gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete=models.SET_NULL,
                                help_text="Select a gallery to link to this club.")
    custom_html = models.TextField(blank=True, null=True, help_text="Add custom HTML to view on club page.")
    slug = models.SlugField(unique=True, help_text="This will be used as URL. /club/slug")
    published = models.BooleanField(default=False)

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
        ('YT', 'YouTube'),
        ('EM', 'Email'),
    )

    FA_CHOICES = (
        ('fa fa-facebook', 'Facebook'),
        ('fa fa-twitter', 'Twitter'),
        ('fa fa-google-plus', 'Google Plus'),
        ('fa fa-instagram', 'Instagram'),
        ('fa fa-github', 'GitHub'),
        ('fa fa-youtube', 'YouTube'),
        ('fa fa-envelope-o', 'Email'),
    )

    IC_CHOICES = (
        ('fb-ic', 'Facebook'),
        ('tw-ic', 'Twitter'),
        ('gplus-ic', 'Google Plus'),
        ('ins-ic', 'Instagram'),
        ('git-ic', 'GitHub'),
        ('yt-ic', 'YouTube'),
        ('email-ic', 'Email'),
    )

    club = models.ForeignKey(Club)
    social_media = models.CharField(max_length=2, choices=SM_CHOICES)
    link = models.URLField
    icon_class = models.CharField(max_length=50, choices=IC_CHOICES)
    fa_icon = models.CharField(max_length=50, choices=FA_CHOICES)

    def __str__(self):
        return self.club.name + self.social_media
