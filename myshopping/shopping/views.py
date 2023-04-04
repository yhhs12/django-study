from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shopping
from django.template import loader



# Create your views here.
def index(request):
    print('index()실행')
    shopping_list = Shopping.objects.all() 
    context = {
        'shopping_list' : shopping_list
    }
    return render(request, 'shopping/main.html', context)

def home(request):
    return HttpResponseRedirect('/shopping/')

def add(request):
    if request.method == 'GET':
        return render(request, 'shopping/order_form.html')
    else:
        item_name = request.POST['item_name']
        item_count = request.POST['item_count']
        
        Shopping.objects.create(
            item_name = item_name,
            item_count = item_count,
        )
        return HttpResponseRedirect('shopping/order_form.html')
    
def read(request, id):
    shopping = Shopping.objects.get(id = id)
    shopping.save()
    
    context = {
        'shopping' : shopping
    }          
    
    return render(request, 'shopping/order_read.html', context)
        
        
def find_text(request):
    input_content = request.POST["search_content"]
    condition = request.POST["condition"]
    
    find_orderList = []
    if condition == "all":
        #전방 일치
        find_orderList = Shopping.objects.filter(item_name = input_content)

        
    else:
        #부분 일치
        find_orderList = Shopping.objects.filter(item_name__contains = input_content)       

    context = {
        'shopping_list' : find_orderList
    }
    return render(request, 'shopping/index.html', context)

def update(request, id):
    shopping = Shopping.objects.get(id = id)
    
    if request.method == "GET":
        context = {'shopping' : shopping}
        return render(request, 'shopping/order_update.html', context)
    
    else:
        shopping.item_name = request.POST['context']
        shopping.item_count = request.POST['count']        
        shopping.save()
        
    return HttpResponseRedirect('/shopping/')

def delete(request, id):
    
    Shopping.objects.get(id=id).delete()    
    
    return HttpResponseRedirect('/shopping/')

def order(request):
    if request.method == 'GET':
        return render(request, 'shopping/index.html')