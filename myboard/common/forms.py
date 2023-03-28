#forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#UserCreationForm을 상속받는 UserForm을 작성
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    first_name = forms.CharField
    last_name = forms.CharField
    class Meta:  #폼의 정보를 담고 있는 내부 클래스
        model = User
        fields = ("username", "email", "first_name", "last_name")
        
        