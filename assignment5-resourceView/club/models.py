from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
Create model classes for the python club database. These should include:

Meeting which will have fields for meeting title, meeting date, meeting time, location, Agenda

Meeting Minutes which will have fields for meeting id (a foreign key), attendance (a many to many field with User), Minutes text

Resource which will have fields for resource name, resource type, URL, date entered, user id (foreign key with User), and description

Event which will have fields for event title, location, date, time, description and the user id of the member that posted it

register the models in admin.py

Create and troubleshoot the models, and then make migrations and migrate

Create a superuser and open the admin site

Upload the code to GitHub and post the url in canvas
'''


class Meeting(models.Model):
    meetingtitle = models.CharField(max_length=255)
    meetingdate = models.DateField()
    meetingtime = models.TimeField()
    meetinglocation = models.CharField(max_length=255)
    meetingagenda = models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table = 'meeting'
        verbose_name_plural = 'meetings'


class Minute(models.Model):
    meetingid = models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendence = models.ManyToManyField(User, related_name='attendence')
    minutestext = models.TextField()

    def __str__(self):
        return self.minutestext

    class Meta:
        db_table = 'minute'
        verbose_name_plural = 'minutes'


class Resource(models.Model):
    resourcename = models.CharField(max_length=255)
    resourcetype = models.CharField(max_length=255)
    resourceurl = models.URLField(null=True, blank=True)
    resourcedate = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resourcedescription = models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table = 'resource'
        verbose_name_plural = 'resources'


class Event(models.Model):
    eventtitle = models.CharField(max_length=255)
    eventlocation = models.CharField(max_length=255)
    eventdate = models.DateField()
    eventtime = models.TimeField()
    eventdescription = models.TextField()
    eventuser = models.ManyToManyField(User, related_name='eventuser')

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table = 'event'
        verbose_name_plural = 'events'
