from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Item
from django.utils import timezone


#def index(request):
 #   return HttpResponse("Hello, world. This is the posts page")

class IndexView(generic.ListView):
	template_name = 'posts/index.html'
	context_object_name = 'latest_post_list'
	
	def get_queryset(self):
		return Item.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:10]

class DetailView(generic.DetailView):
	model = Item
	template_name = 'posts/detail.html'
	
	def get_queryset(self):
		return Item.objects.filter(pub_date__lte=timezone.now())

#def details(request):
#	return HttpResponse("this is the detail page for a post")#