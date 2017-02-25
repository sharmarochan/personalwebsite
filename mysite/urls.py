from django.conf.urls import url
from mysite import views

urlpatterns = [
     url(r'^home/$', views.home, name='home'),
]