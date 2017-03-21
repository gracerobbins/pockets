from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Item
from django.utils import timezone
from .forms import ItemForm
import os


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

def new_item(request):
	template_name = 'posts/form.html'


	#return HttpResponse("this is where a new item form goes")
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ItemForm(request.POST, request.FILES)
		# check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			form_name = form.cleaned_data['name']
			form_description = form.cleaned_data['description']
			form_link = form.cleaned_data['form_link']
			form_price = form.cleaned_data['form_price']
			form_image = form.cleaned_data['image']
		#	handle_uploaded_file(request.FILES['file'])
			new_item = Item(item_name=form_name, item_description=form_description, pub_date=timezone.now(), link=form_link, price=form_price, image=form_image)
			print new_item
			new_item.save()
			# redirect to a new URL:
			return HttpResponseRedirect(reverse('posts:index'))

	#if a GET (or any other method) we'll create a blank form
	else:
		form = ItemForm()

	return render(request, 'posts/form.html', {'form': form})
'''class NewItemView(generic.ListView):
	template_name = 'posts/form.html'
	
	def post(self):
		return self.submit()

	def submit(request):
		#return HttpResponse("this is where a new item form goes")
		# if this is a POST request we need to process the form data
		if request.method == 'POST':
			# create a form instance and populate it with data from the request:
			form = ItemForm(request.POST)
			# check whether it's valid:
			if form.is_valid():
				# process the data in form.cleaned_data as required
				form_name = form.cleaned_data['name']
				form_description = form.cleaned_data['description']
				form_link = form.cleaned_data['form_link']
				form_price = form.cleaned_data['form_price']
				new_item = Item(item_name=form_name, item_description=form_description, pub_date=timezone.now(), link=form_link, price=form_price)
				print new_item
				new_item.save()
				# redirect to a new URL:
				return HttpResponseRedirect('https://docs.djangoproject.com/en/1.10/topics/forms/')

		#if a GET (or any other method) we'll create a blank form
		else:
			form = ItemForm()

		return render(request, 'posts/form.html', {'form': form})'''
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
def gallery(request):
    path='../mysite/media/itemjielksmek'  # insert the path to your directory   
    img_list =os.listdir(path)   
    return render_to_response('detail.html', {'images': img_list})
