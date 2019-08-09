from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home
 
urlpatterns = [
    path('home', home, name ="player_home"),
    path('login',LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
    path('logout', LogoutView.as_view(template_name=""), name="player_logout"),
]