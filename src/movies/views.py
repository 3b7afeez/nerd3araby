from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
def home_view(request):
	template_name = 'movies/home.html'
	return render(request, template_name)