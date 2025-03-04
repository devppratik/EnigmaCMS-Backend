from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]

YEAR_CHOICES = [
    ('1', 'First'),
    ('2', 'Second'),
    ('3', 'Pre-Final'),
    ('4', 'Final'),
    ('5', 'Alumni'),
]

class Event(models.Model):
    name = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    poster = models.ImageField(upload_to='EventPosters', default='DefaultEventPoster.jpg')
    slug = models.CharField(unique=True, max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    registration_start_date = models.DateField(null=True, blank=True)
    registration_end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        slug_eixts = Event.objects.filter(slug=self.slug).exists()
        if slug_eixts:
            num = Event.objects.filter(name=self.name).count()
            self.slug += '-' + str(num + 1)
        super(Event, self).save(*args, **kwargs)



class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique = True)
    year = models.CharField(max_length=15)
    branch = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=8)
    whatsapp_no = models.CharField(max_length=15,unique = True)
    expectations = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    reg_number = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.firstname 
