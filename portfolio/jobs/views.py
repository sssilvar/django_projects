from django.shortcuts import render

from .models import Job


def home(request):
    jobs = Job.objects
    data = {
        'site': 'Home',
        'jobs': jobs
    }
    return render(request, 'jobs/home.html', data)
