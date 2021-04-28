from django.contrib import admin
from .models import Winner, Category, Match_1_Winner

# Register your models here.
admin.site.register(Winner)
admin.site.register(Category)
admin.site.register(Match_1_Winner)