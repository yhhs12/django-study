from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, Order
from django.template import loader

# Create your views here.
def main(request):    
    return render(request, 'shopping/main.html')

def order(request):
    order_list = Order.objects.all()
    context ={
        'order_list' : order_list
    }
    if request.method == 'GET':
        return render(request, 'shopping/order_list.html', context)
    
def add(request):
    if request.method == 'GET':
        return render(request, 'shopping/order_form.html')
    else:
        item_name = request.POST['item']
        quantity = request.POST['quantity']
    
        item, created = Item.objects.get_or_create(item_name=item_name)
        order = Order.objects.create(
            item=item,
            quantity=quantity,
        )
        return HttpResponseRedirect('/order/')
    
def read(request, id):
    order_list = Order.objects.get(id = id)
    order_list.save()
    
    context = {
        'order_list' : order_list
    }          
    
    return render(request, 'shopping/order_read.html', context)
    
    