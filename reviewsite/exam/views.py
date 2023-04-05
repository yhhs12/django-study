from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from django.template import loader
from django.core.paginator import Paginator


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
    
    return render(request, 'exam/index.html', context)  # 컨텍스트 변수를 템플릿에 전달하여 렌더링
        
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
        genre = request.POST['genre']
        description = request.POST['description']
        movie_name = request.POST['title']
        
        movie = Movie(genre=genre, movie_name=movie_name, movie_summary=description)
        movie.save()
        
        
    return HttpResponseRedirect('/exam/')
        


    
        