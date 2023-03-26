from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Coffee
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse



# Create your views here.

def home(request):
    return HttpResponseRedirect('/coffee/')

def index(request):
        
    order_list = Coffee.objects.all()
    
    context = {
        'order_list' : order_list
    }
    return render(request, 'coffee/index.html', context)

def add(request):
    if request.method == 'GET':
        return render(request, 'coffee/order_form.html')
    else:
        order_text = request.POST['order_text']
        price = request.POST['price']
        address = request.POST['address']
       
        Coffee.objects.create(
            order_text = order_text,
            price = price,
            address = address,
        )
        return HttpResponseRedirect('/coffee')
    
def read(request, id):
    coffee = Coffee.objects.get(id = id)
    coffee.save()
    
    context = {
        'coffee' : coffee
    }          
    
    return render(request, 'coffee/order_read.html', context)    

def find_ordertext(request):
    input_content = request.POST["search_content"]
    condition = request.POST["condition"]
    
    find_orderList = []
    if condition == "all":
        #전방 일치
        find_orderList = Coffee.objects.filter(order_text = input_content)

        
    else:
        #부분 일치
        find_orderList = Coffee.objects.filter(order_text__contains = input_content)       

    context = {
        'order_list' : find_orderList
    }
    return render(request, 'coffee/index.html', context)

def update(request, id):
    coffee = Coffee.objects.get(id = id)
    
    if request.method == "GET":
        context = {'coffee' : coffee}
        return render(request, 'coffee/order_update.html', context)
    
    else:
        coffee.order_text = request.POST['context']
        coffee.price = request.POST['price']
        coffee.address = request.POST['address']
        
        coffee.save()
        
    return HttpResponseRedirect('/coffee/')

def delete(request, id):
    
    Coffee.objects.get(id=id).delete()    
    
    return HttpResponseRedirect('/coffee/') 


def logout(request):
    request.session.pop('user', None)
    return HttpResponseRedirect('/')
   
def login(request):
    if request.method == 'GET':
        return render(request, 'coffee/login_form.html')
    
    elif request.method == 'POST':
        username = request.POST.get('userName')
        password = request.POST.get('userPassword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['user'] = username
            return HttpResponseRedirect(reverse('coffee'))
        else:
            error_message = "로그인 실패"
            return render(request, 'coffee/login.html', {'error_message': error_message})
    else:
        return render(request, 'coffee/login.html', {'error_message': error_message})
    

def signup(request):
        if request.method == 'GET':
            return render(request, 'coffee/signup_form.html')
        
        elif request.method == 'POST':
            username = request.POST['userName']
            password1 = request.POST['userPassword']
            password2 = request.POST['userPassword2']
            
            if password1 != password2:
                return render(request, 'coffee/signup_form.html', {'error': '비밀번호가 일치하지 않습니다'})
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
            except:
                return render(request, 'coffee/signup_form.html', {'error': '회원가입 실패!'})
            
            return redirect(reverse('coffee:login'))
        

        
        
        # #응답 데이터
        # res_data = {}
        # #모든 필드를 채우지 않았을 경우
        # if not (userName and password):
        #     res_data['error'] = '모든 값을 입력해 주세요.'
        # #모든 필드를 채웠을 경우
        # else:
        #     user = User.objects.get(userName=userName)
        #     if check_password(password, user.password):
        #         request.session['user'] = user.id
        #         return HttpResponseRedirect('/')
        
    
