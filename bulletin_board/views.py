from django.shortcuts import render, get_object_or_404
from .models import Bulletin
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):
    bulletin_list = Bulletin.objects.all().order_by('-writeDate')
    context = {'bulletin_list': bulletin_list}
    return render(request, 'bulletin/index.html', context)

def create_bulletin(request):
    return render(request, 'bulletin/create_bulletin.html')

def add_bulletin(request):
    bulletin = Bulletin()
    bulletin.title = request.POST['title']
    bulletin.content = request.POST['content']
    bulletin.name = request.POST['name']
    bulletin.passwd = request.POST['pincode']
    bulletin.save()

    return HttpResponseRedirect(reverse('bulletin_board:index'))

def view_bulletin(request, bulletin_id):
    bulletin = get_object_or_404(Bulletin, pk=bulletin_id)
    return render(request, 'bulletin/detail.html', {'bulletin':bulletin})