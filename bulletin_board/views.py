from django.shortcuts import render
from .models import Bulletin
# Create your views here.

def index(request):
    bulletin_list = Bulletin.objects.all().oredr_by('-writeDate')