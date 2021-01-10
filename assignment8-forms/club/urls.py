from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
    path('resourcedetails/<int:id>', views.resourcedetails, name='r_details'),
    path('meetings/', views.meetings, name='meetings'),
    path('meetingdetails/<int:id>', views.meetingdetails, name='details'),
    path('newresource/', views.newResource, name='newresource'),
    path('newmeeting/', views.newMeeting, name='newmeeting'),
]
