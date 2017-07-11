from django.db import models
from django.db.models import Q
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from versatileimagefield.fields import VersatileImageField


class KonnektQueryset(models.query.QuerySet):
    def search(self, query):
        if query:
            return self.filter(Q(skills__icontains=query)|
                               Q(user__first_name__icontains=query)|
                               Q(user__last_name__icontains=query)
                               ).distinct()
        else:
            return self


class UserProfileManager(models.Manager):
    def get_queryset(self):
        return KonnektQueryset(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)


class UserProfile(models.Model):
    # Validators
    valid_year = RegexValidator(r'^[0-9]{4}$', message='Not a valid year!')
    contact = RegexValidator(r'^[0-9]{10}$', message='Not a valid number!')
    # Choices
    PROG_CHOICES = (
        ('BT', 'B.Tech'),
        ('MT', 'M.Tech'),
        ('PhD', 'PhD')
    )
    YEAR_CHOICES = (
        # ('0', 'Alumni'),
        ('1', 'First Year'),
        ('2', 'Second Year'),
        ('3', 'Third Year'),
        ('4', 'Fourth Year')
    )
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'Transgender'),
    )
    BRANCH_CHOICES = (
        ('CSE', 'Computer Science and Engineering'),
        ('EE', 'Electrical Engineering'),
        ('ME', 'Mechanical Engineering'),
    )

    # Database Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    roll = models.CharField(max_length=15, unique=True)
    dob = models.DateField()
    prog = models.CharField(max_length=5, choices=PROG_CHOICES, verbose_name='programme', default='BT')
    year = models.CharField(max_length=1, choices=YEAR_CHOICES, default='1')
    phone = models.CharField(max_length=10, validators=[contact])
    avatar = VersatileImageField(upload_to='avatar', blank=True, null=True)
    cover = VersatileImageField(upload_to='cover', blank=True, null=True)
    hometown = models.CharField(max_length=128)
    branch = models.CharField(max_length=5, choices=BRANCH_CHOICES)
    skills = models.TextField(help_text="Enter your skills, separated by comma.", max_length=1024, blank=True,
                              null=True)
    about = models.TextField(max_length=160, verbose_name='about you', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('oauth:detail', kwargs={'pk': self.pk})

    objects = UserProfileManager()

    def __str__(self):
        return self.roll + " (" + self.user.get_full_name() + ")"

    @property
    def skills_as_list(self):
        if self.skills == '':
            return ''
        return self.skills.split(',')


class SocialLink(models.Model):
    SM_CHOICES = (
        ('FB', 'Facebook'),
        ('TW', 'Twitter'),
        ('LI', 'LinkedIn'),
        ('GP', 'Google Plus'),
        ('IG', 'Instagram'),
        ('GH', 'GitHub'),
        ('YT', 'YouTube'),
    )
    FA_CHOICES = (
        ('fa fa-facebook', 'FB'),
        ('fa fa-twitter', 'TW'),
        ('fa fa-linkedin', 'LI'),
        ('fa fa-google-plus', 'GP'),
        ('fa fa-instagram', 'IG'),
        ('fa fa-github', 'GH'),
        ('fa fa-youtube', 'YT'),
    )
    IC_CHOICES = (
        ('fb-ic', 'FB'),
        ('tw-ic', 'TW'),
        ('li-ic', 'LI'),
        ('gplus-ic', 'GP'),
        ('ins-ic', 'IG'),
        ('git-ic', 'GH'),
        ('yt-ic', 'YT'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    social_media = models.CharField(max_length=2, choices=SM_CHOICES)
    link = models.URLField()

    class Meta:
        ordering = ['social_media']

    def __str__(self):
        return self.user.get_full_name() + ' - ' + self.get_social_media_display()

    def get_fai(self):
        for key, value in self.FA_CHOICES:
            if value == self.social_media:
                return key
        return 'fa fa-link'

    def get_sm_ic(self):
        for key, value in self.IC_CHOICES:
            if value == self.social_media:
                return key
        return ''
