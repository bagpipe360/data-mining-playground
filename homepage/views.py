import json
from homepage.k_means.k_means import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.

from django.shortcuts import render


def index(request):
    return render(request, 'homepage/index.html', {})


def k_means(request):
    return render(request, 'homepage/k_means.html', {})

@csrf_exempt
def k_means_graph_json(request):
    k = int(request.POST['k'])
    csv = json.loads(request.POST['csv'])
    graphing_data = draw_k_means(k, csv)

    return HttpResponse(json.dumps(graphing_data), content_type="application/json")