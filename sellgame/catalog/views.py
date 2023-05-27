from django.shortcuts import render, HttpResponse
from .models import *


def catalog(request):
    cat = Catalog.objects.filter(is_published=True).order_by('name')
    return render(request, 'catalog.html', {'cat': cat})


def show_post(request, post_id):
    return HttpResponse(f"Отображение игры с id = {post_id}")
