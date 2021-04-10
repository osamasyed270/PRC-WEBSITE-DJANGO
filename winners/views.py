from django.shortcuts import render, HttpResponse
from django.db import models
from winners.models import Winner, Category

# Create your views here.
def winners_home(request):
    category_list = Category.objects.all()
    allwinners = Winner.objects.all()
    context = {'allwinners': allwinners, 'category_list':category_list}
    return render(request, 'winners/winners-home.html', context)

def match_details(request, cats):
    category_posts = Winner.objects.filter(categories=cats.replace('-', ' ')) 
    return render(request, 'winners/match-details.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

