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