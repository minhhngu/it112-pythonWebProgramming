from django.shortcuts import render, get_object_or_404
from .models import Meeting, Minute, Resource, Event
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    return render(request, 'club/index.html')


def resources(request):
    resource_list = Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})


def meetings(request):
    meetings = Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meetings': meetings})


def meetingdetails(request, id):
    details = get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetails.html', {'details': details})
