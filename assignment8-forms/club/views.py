from django.shortcuts import render, get_object_or_404
from .models import Meeting, Minute, Resource, Event
from django.urls import reverse_lazy
from .forms import ResourceForm, MeetingForm

# Create your views here.


def index(request):
    return render(request, 'club/index.html')


def resources(request):
    resources = Resource.objects.all()
    return render(request, 'club/resources.html', {'resources': resources})


def resourcedetails(request, id):
    r_details = get_object_or_404(Resource, pk=id)
    return render(request, 'club/resourcedetails.html', {'r_details': r_details})


def meetings(request):
    meetings = Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meetings': meetings})


def meetingdetails(request, id):
    details = get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetails.html', {'details': details})


def newResource(request):
    form = ResourceForm

    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form. is_valid():
            post = form.save(commit=True)
            post.save()
            form = ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})


def newMeeting(request):
    form = MeetingForm

    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form. is_valid():
            post = form.save(commit=True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})
