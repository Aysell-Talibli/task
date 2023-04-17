from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.add_instagram, name='login'),
    path('add_username',views.add_username, name='add_username'),
]