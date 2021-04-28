from django.shortcuts import render, HttpResponse
from django.db import models
from winners.models import Winner, Category, Match_1_Winner

# Create your views here.
def winners_home(request):
    allwinners = Winner.objects.all()

    match1 = Match_1_Winner.objects.all().order_by('timestamp')[:5]
    match1detail = Match_1_Winner.objects.all()

    context = {
        'allwinners': allwinners,
        'match1': match1,
        'match1detail': match1detail
    }

    return render(request, 'winners/winners-home.html', context)

def match_details(request, cats):
    category_posts = Winner.objects.filter(categories=cats.replace('-', ' ')) 
    return render(request, 'winners/match-details.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

