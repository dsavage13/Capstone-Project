from django.shortcuts import render
from django.template.loader import render_to_string

def home_view(request):
    return render(request, 'base.html')

def about_view(request):
    return render(request, 'about.html')