from django.conf.urls import url
from . import views

app_name = 'posts'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[A-Za-z0-9_]+)/$', views.DetailView.as_view(), name='detail')
]