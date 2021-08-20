from django.urls import path
from app import views

urlpatterns = [
    path ('', views.home, name='index'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('tweet', views.create_tweet, name='tweet'),
]