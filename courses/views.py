from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    template_name = 'courses/index.html'
    return render(request, template_name, context)

def details(request, id):
    course = Course.objects.get(id=id)
    context = {
        'course': course
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)