from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, Minute, Resource, Event
import datetime
from django.urls import reverse_lazy, reverse
from .forms import ResourceForm, MeetingForm

# Create your tests here.


class MeetingTest(TestCase):
    def setUp(self):
        self.type = Meeting(meetingtitle='Learn Python 101')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Learn Python 101')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MinuteTest(TestCase):
    def setUp(self):
        self.type = Minute(minutestext='Did a bunch of cool things')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Did a bunch of cool things')

    def test_tablename(self):
        self.assertEqual(str(Minute._meta.db_table), 'minute')


class ResourceTest(TestCase):
    def setUp(self):
        self.type = Resource(resourcename='pencil')

    def test_string(self):
        self.assertEqual(str(self.type), 'pencil')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


class EventTest(TestCase):
    def setUp(self):
        self.type = Event(eventtitle='Lunar New Year')

    def test_string(self):
        self.assertEqual(str(self.type), 'Lunar New Year')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')


class NewResourceForm(TestCase):
    def test_resourceform(self):
        data = {
            'resourcename': 'Pencils',
            'resourcetype': 'Stationary',
            'resourceurl': 'http://www.microsoft.com',
            'resouredate': '2021-1-9',
            'user': 'minh',
            'resourcedescription': 'Bought some pencils',
        }

        form = ResourceForm(data)
        self.assertTrue(form.is_valid)

    # this test is failing
    def test_ResourceForm_Invalid(self):
        data = {
            'resourcename': 'Pencils',
            'resourcetype': "",
            'resourceurl': 'http://pencil.com',
            'user': 'minh',
            'resourcedescription': 'Bought some pencils',
        }

        form = ResourceForm(data)
        self.assertFalse(form.is_valid)


class NewMeetingForm(TestCase):
    def test_meetingform(self):
        data = {
            'meetingtitle': 'Learn Python 101',
            'meetingdate': '2020-01-09',
            'meetingtime': '18:00:00',
            'meetinglocation': 'Seattle, WA',
            'meetingagenda': 'Learn Python coding basics',
        }

        form = ResourceForm(data)
        self.assertTrue(form.is_valid)
