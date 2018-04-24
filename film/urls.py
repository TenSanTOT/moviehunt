from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.FilmListView.as_view(), name='home'),
    path('vote/<int:pk>/', views.vote, name='vote'),
    path('film/<int:pk>/', views.film_detail, name='film_detail'),
    path('recommend/', login_required(views.Recommend.as_view()), name='recommend'),
]
