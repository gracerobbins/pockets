from django.conf.urls import url
from . import views

app_name = 'posts'
urlpatterns = [
#    url(r'^form/', views.NewItemView.as_view(), name='form'),
	url(r'^form/', views.new_item, name='form'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^', views.IndexView.as_view(), name='index'),
    
]