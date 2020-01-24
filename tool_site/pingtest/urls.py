from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='ping-test'),
    # path('runtest', views.run_test, name='run-test'),
]