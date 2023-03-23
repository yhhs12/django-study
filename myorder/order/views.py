from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Order
# Create your views here.

def home(request):
    return HttpResponseRedirect('/order/')

def index(request):
    print('index()실행')
    
    order_list = Order.objects.all()
    
    context = {
        'order_list' : order_list
    }
    return render(request, 'order/index.html', context)

def find_ordertext(request):
    input_content = request.POST["search_content"]
    condition = request.POST["condition"]
    
    find_orderList = []
    if condition == "all":
        #전방 일치
        find_orderList = Order.objects.filter(contenet = input_content)

        
    else:
        #부분 일치
        find_orderList = Order.objects.filter(content__contains = input_content)       

    context = {
        'ordertext' : find_orderList
    }
    return render(request, 'order/index.html', context)

def add(request):
    if request.method == 'GET':
        return render(request, 'order/order_form.html')
    else:
        order_text = request.POST['order_text']
        price = request.POST['price']
        address = request.POST['address']
       
        Order.objects.create(
            order_text = order_text,
            price = price,
            address = address,
        )
        return HttpResponseRedirect('/')
    
def update(request, id):
    order = Order.objects.get(id = id)
    
    if request.method == "GET":
        context = {'order' : order}
        return render(request, 'order/order_update.html', context)
    
    else:
        order.order_text = request.POST['context']
        order.price = request.POST['price']
        order.address = request.POST['address']
        
        order.save()
        
    return HttpResponseRedirect('/order/')

def read(request, id):
    order = Order.objects.get(id = id)
    order.save()
    
    context = {
        'order' : order
    }          
    
    return render(request, 'order/order_read.html', context)

def delete(request, id):
    
    Order.objects.get(id=id).delete()    
    
    return HttpResponseRedirect('/order/')                         
