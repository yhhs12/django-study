from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Coffee

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
    
