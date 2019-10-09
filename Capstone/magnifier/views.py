from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.utils.six import BytesIO
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.template import loader
import os
from django.utils import datastructures
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    context = {
        'title':'well come to magnifier',
    }
    return render(request, 'index.html', context)

def upload_image(request):
    up_img = request.FILES['up_img']

    # write file to the media folder
    file_path = os.path.join('upload_image', up_img.name)
    with open(os.path.join(settings.MEDIA_ROOT, file_path), 'wb') as f:
        for chunk in up_img.chunks():
            f.write(chunk)

    # result image file path
    result_file_path = os.path.join('result_image', up_img.name)
    with open(os.path.join(settings.MEDIA_ROOT, result_file_path), 'wb') as f:
        for chunk in up_img.chunks():
            f.write(chunk)
    # allow the frontend to access the uploaded media
    context = {
        'up_img_url':os.path.join('../media/', file_path),
        'res_img_url':os.path.join('../media/',result_file_path),
    }

    return render(request, 'result.html', context)
