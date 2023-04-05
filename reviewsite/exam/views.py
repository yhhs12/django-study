from json import loads
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from django.template import loader
from django.core.paginator import Paginator
from django.db.models import Avg


from .models import Movie, Review

# Create your views here.

def index(request):
    result = None
    
    context = {}
    
    movie_list = Movie.objects.all().order_by('-id')
        
    return render(request, 'exam/index.html', context)
    
def add(request):
    if request.method == 'POST':
        genre = request.POST['genre']
        title = request.POST['title']
        description = request.POST['description']

        
        movie = Movie(genre=genre, movie_name=title, movie_summary=description)
        movie.save()
    else:        
        return render(request, 'exam/add_form.html')
    return HttpResponseRedirect('/exam/')


    
def movie_list(request):
    movies = Movie.objects.all()
    
    result = None
    
    context = {}
    
    movie_list = Movie.objects.all().order_by('-id')
    
    context = {'movie_list': movies}
    
    return render(request, 'exam/movie_list.html', context)
        
def read(request, id):
    movie = Movie.objects.get(id = id)
    
    
    review_list = Review.objects.filter(reviewer_name = id).order_by('-id')
    
    context = {
        'movie' : movie,
        'reviewList' : review_list
    }
    
    return render(request, 'exam/read.html', context)

def update(request, id):
    movie = Movie.objects.get(id = id)
    
    if request.method == "GET":
        context = {'movie' : movie}
        return render(request, 'exam/movie_update.html', context)
    
    else:
        movie.genre = request.POST['genre']
        movie.movie_summary = request.POST['description']
        movie.movie_name = request.POST['title']       
        
        movie.save()
        
        
    return HttpResponseRedirect('/exam/')

def delete(request, id):
    
    movie = Movie.objects.get(id=id)
    movie.delete()
    return HttpResponseRedirect('/exam/')



def write_review(request, id):
    movie = Movie.objects.get(id=id)
    
    if request.method == 'POST':
        reviewer_name = request.POST['nickname']
        review_text = request.POST['description']
        score = request.POST['score']   
        
        review = Review(reviewer_name=reviewer_name, review_text=review_text, score=score, movie=movie)
        review.save()
    
    context = {
        'movie': movie,
        'review': review  
    }

    return HttpResponseRedirect('/exam/' + str(id), context)





    
        