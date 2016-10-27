from django.conf.urls import url
from data_mining_playground import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^k-means', views.k_means, name='k_means'),
]

