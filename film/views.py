from django.views.generic import ListView, CreateView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from . models import Film
from .forms import CommentForm
from django.utils import timezone

class FilmListView(ListView):
    model = Film
    template_name = 'home.html'

def vote(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.user.is_authenticated:
        likes = film.like.all()
        if request.user in likes:
            pass
        else:
            if request.user.is_superuser:
                film.vote += 5
                film.like.add(request.user)
            else:
                film.vote += 1
                film.like.add(request.user)
            film.save()
        return redirect('home')
    else:
        return redirect('login')

def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    context = {'film': film, 'form':CommentForm}
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.author = request.user
                comment.film = film
                comment.added = timezone.now()
                comment.save()
                return render(request, 'film/film_detail.html', context)
            else:
                return redirect('login')
        else:
            return render(request, 'film/film_detail.html', context)
    else:
        return render(request, 'film/film_detail.html', context)

class Recommend(CreateView):
    model = Film
    template_name = 'film/recommend.html'
    fields = ['name', 'description','country', 'cover']
    success_url = reverse_lazy('home')
