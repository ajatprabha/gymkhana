from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from versatileimagefield.fields import VersatileImageField


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
        ('0', 'Alumni'),
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
    avatar = VersatileImageField(upload_to='avatar')
    cover = VersatileImageField(upload_to='cover', blank=True, null=True)
    hometown = models.CharField(max_length=128)
    branch = models.CharField(max_length=5, choices=BRANCH_CHOICES)
    skills = models.TextField(help_text="Enter your skills, separated by comma.", max_length=1024)
    about = models.TextField(max_length=512, verbose_name='about you')

    def get_absolute_url(self):
        return reverse('oauth:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.roll + " (" + self.user.get_full_name() + ")"

    @property
    def skills_as_list(self):
        return self.skills.split(',')
