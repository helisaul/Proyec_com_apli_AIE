from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import UsuarioForm 
from .utils import cookieCart , cartData ,guestOrder

import json
import datetime

from django.http import JsonResponse
# Create your views here.


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo después de guardar los datos del usuario
    context = {'form':form}
    return render(request, 'Generales/register.html', context)














def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    

    products = Product.objects.all()
    return render(request,'Generales/store.html',{"products": products ,'cartItems':cartItems})








def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    context = {'items': items, 'order':order,'cartItems': cartItems}
    return render(request,'Generales/cart.html',context)

def checkout(request):
    
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order':order,'cartItems':cartItems}

    
    return render(request,'Generales/checkout.html',context)





def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('productId',productId)

    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order = order,product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added',safe=False)



def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
       

       
    else:

        customer , order = guestOrder(request,data)
    

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
            order.complete = True
    order.save()
    if order.shipping == True:
            ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
            



            )
    return JsonResponse('Pago completado !',safe=False)























