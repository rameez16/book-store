
from django.shortcuts import redirect,render
from django.contrib import messages

from django.http.response import JsonResponse
from store.models import ProductItem,Cart


def index(request):
    
    user=request.user
    
    if user.is_authenticated:
        
        cartitems=Cart.objects.filter(user=user)
        
        bill_amount=0
        
        for item in cartitems:
            
            bill_amount+=item.product.selling_price*item.product_qty
            
        context={'cart':cartitems,'bill_amount':bill_amount}
        
        return render(request,"store/checkout.html",context)  
    
    else:
        return JsonResponse({'status':'user not authenticated'})  
    

    
    