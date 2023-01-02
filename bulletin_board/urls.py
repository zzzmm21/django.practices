from django.urls import path
from . import  views

app_name = 'bulletin_board'
urlpatterns = [
    path('', views.index, name='index'),

]