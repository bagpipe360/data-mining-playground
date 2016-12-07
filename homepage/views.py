import json
from homepage.k_means.k_means import *
from homepage.cart.cart import  *
from homepage.svm.svm import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import os
import csv
from data_mining_playground.settings import PROJECT_ROOT
# Create your views here.

from django.shortcuts import render


def index(request):
    return render(request, 'homepage/index.html', {})


def k_means(request):
    return render(request, 'homepage/k_means.html', {})

def k_means_graph_json(request):
    k = int(request.POST['k'])
    load_sample = request.POST['load_sample']
    if load_sample:
        csvfile = open(os.path.join(PROJECT_ROOT, 'college_score_card.csv'), 'r')
        reader = csv.reader(csvfile)
        csv_data = list(reader)
    else:
        csv_data = json.loads(request.POST['csv'])

    graphing_data = draw_k_means(k, csv_data)

    return HttpResponse(json.dumps(graphing_data), content_type="application/json")


def cart(request):
    return render(request, 'homepage/cart.html', {})

def cart_graph_json(request):
    graphing_data = draw_cart()
    return HttpResponse(json.dumps(graphing_data), content_type="application/json")

def svm(request):
    return render(request, 'homepage/svm.html', {})

def svm_graph_json(request):
    graphing_data = draw_cart()
    return HttpResponse(json.dumps(graphing_data), content_type="application/json")
