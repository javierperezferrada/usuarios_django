from django.conf.urls import patterns, url
from django.contrib.auth.views import login,logout
 
 
urlpatterns = patterns('',
                       url(r'^$', 'myapp.views.main', name='main'),
                       url(r'^signup$', 'myapp.views.signup', name='signup'),
                       url(r'^login$', login, {'template_name': 'login.html', }, name="login"),
                       url(r'^home$', 'myapp.views.home', name='home'),
                       url(r'^logout$', logout, {'template_name': 'main.html', }, name="logout"),
)