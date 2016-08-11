from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context

# Create your views here.
def index(request) :
    return render_to_response('index.html', Context())