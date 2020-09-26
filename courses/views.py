from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import ContactCourse

# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    template_name = 'courses/index.html'
    return render(request, template_name, context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    if request.POST:
        form = ContactCourse(request.POST)
    else:
        form = ContactCourse()
    context = {
        'course': course,
        'form': form
    }
    template_name = 'courses/details.html'
    return render(request, template_name, context)