from django.urls import path
from .views import game_detail, make_move

urlpatterns = [
    path('detail/<id>', game_detail, name='gameplay_detail'),
    path('make_move/<id>', make_move, name='gameplay_make_move')
]
