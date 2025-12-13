
from django.shortcuts import redirect,render
from django.contrib import messages
import random

from django.http.response import JsonResponse
from store.models import ProductItem,Cart,User,Profile,Order,OrderItem



def order(request):
    
    orders=Order.objects.filter(user=request.user)
    
    selected_order=None
    order_items = None 
    
    tracking_no=request.GET.get('tracking_no')
    
    if tracking_no:
        selected_order=Order.objects.filter(user=request.user,tracking_no=tracking_no).first()
        order_items=OrderItem.objects.filter(order=selected_order)
    
    context={'orders':orders,'selected_order':selected_order,'order_item':order_items}
    
    return render(request,"store/order.html",context)
    