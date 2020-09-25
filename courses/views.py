from django.shortcuts import render, get_object_or_404
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
    course = get_object_or_404(Course, id=id)
    context = {
        'course': course
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)