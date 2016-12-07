from django.conf.urls import url
from data_mining_playground import settings

from homepage.k_means.k_means import *
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^k-means', views.k_means, name='k_means'),
    url(r'^k_means_graph_json', views.k_means_graph_json, name='k_means_graph_json'),
    url(r'^cart$', views.cart, name='cart'),
    url(r'^cart_graph_json', views.cart_graph_json, name='cart_graph_json'),
    url(r'^svm$', views.svm, name='svm'),
    url(r'^svm_graph_json', views.svm_graph_json, name='svm_graph_json'),

]

