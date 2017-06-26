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
    roll = models.CharField(max_length=15)
    dob = models.DateField()
    enroll_year = models.CharField(max_length=4, validators=[valid_year])
    phone = models.CharField(max_length=10, validators=[contact])
    avatar = VersatileImageField(upload_to='avatar')
    hometown = models.CharField(max_length=128)
    branch = models.CharField(max_length=5, choices=BRANCH_CHOICES)
    about = models.CharField(max_length=512)

    def get_absolute_url(self):
        return reverse('oauth:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.roll + " (" + self.user.get_full_name() + ")"

    @property
    def get_gender(self):
        return self.get_gender_display()

    @property
    def get_branch(self):
        return self.get_branch_display()

