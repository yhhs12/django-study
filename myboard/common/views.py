from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
# 장고가 제공하는 기본 회원가입 폼
from django.contrib.auth.forms import UserCreationForm

#우리가 만든 커스텀 회원가입 폼
from .forms import UserForm

# Create your views here.

def index(request): 
    
    # 아까 만든 common/index.html을 표시하고
    # localhost:8000/으로 들어갔을 때
    # 잘 표시가 되는지 확인
    
    return render(request, "common/index.html")

def signup(request):
    
    if request.method == 'POST':
        #요청 객체가 담고 있는 정보로 사용자 생성 폼 만든다.
        print(request.POST)
        form = UserCreationForm(request.POST)
        
        if form.is_valid(): #form의 내용이 유효하다면
            form.save()  #DB에 폼 정보 저장
            
            #폼에 입력한 값 가져오기
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            #사용자 인증
            user = authenticate(username=username, password=raw_password)
            
            #로그인
            login(request, user)
            
            return redirect('/')
    else:
        #GET 방식으로 요청이 오면 비어있는 사용자 생성 폼을 만든다.
        form = UserCreationForm()
    
    return render(request, 'common/signup.html', {'form' : form})

def signup_custom(request):
    if request.method == "POST":
        print(request.POST)    #QueryDict 한번 보기
        
        #request.POST에 들어있는 정보를 UserForm 형식으로 변환 
        form = UserForm(request.POST)
        
        #form이 유효한가?
        if form.is_valid():
            form.save()  #form의 내용을 DB에 바로 저장
            
            #폼의 정보 취득   #폼 객체 내용을 가져올때 .cleaned_data()함수를 사용
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            #사용자 인증 후 로그인
            user = authenticate(username=username, password=raw_password, first_name=first_name, last_name=last_name)
            login(request, user)
            
            return redirect('/')  #로그인 후 메인 페이지로 넘김

    else: #요청이 get일때
        form = UserForm()  #새 폼 만들어주기
        
    return render(request, 'common/signup.html', {'form' : form})