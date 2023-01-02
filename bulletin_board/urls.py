from django.urls import path
from . import  views

app_name = 'bulletin_board'
urlpatterns = [
    path('', views.index, name='index'),
    path('create',views.create_bulletin, name='new_bulletin'),
    path('add',views.add_bulletin, name='insert_bulletin'),

]