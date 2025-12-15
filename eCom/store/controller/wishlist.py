
from django.shortcuts import redirect,render
from django.contrib import messages

from django.http.response import JsonResponse

from store.models import ProductItem,Cart,User,Wishlist




def index(request):
    
    if not request.user.is_authenticated:
        message="You are not Logged in"
        context={'message':message}
        return render(request,'store/wishlist.html',context)
    
    wishlist=Wishlist.objects.filter(user=request.user)
    wishlist_count = wishlist.count()

    context = {
        'wishlist': wishlist,
        'wishlist_count': wishlist_count,
    }
    
    
    return render(request,'store/wishlist.html',context)




def add_to_wishlist(request):
    
    if request.method=='POST':
        user=request.user
        
        if user.is_authenticated:
            
            prod_id=request.POST.get('product_id')
            
            product=ProductItem.objects.get(id=prod_id)
            
            if(product):
                
                if(Wishlist.objects.filter(product__id=prod_id,user=user)):
                    
                    return JsonResponse({'status':'Products already inside wishlist'})
                
                else:
                    
                    Wishlist.objects.create(product=product,user=user)
                    return JsonResponse({"status":"Product added to wishlist!"})
                    
            else:
                return JsonResponse({"status":'Product do not exists'})
            
               
        else:
            return JsonResponse({'status':'User not logged in'})  
    
    
    return redirect('/')   






def move_item_to_cart_from_wishlist(request):
    
    
    user=request.user
    
    if request.method=='POST':
        
        if user.is_authenticated:
            
            wishlist_item=Wishlist.objects.filter(user=user)
            
            
            for item in wishlist_item:
                
                if not Cart.objects.filter(user=user,product=item.product).exists(): #   Check if product already in cart
                    
                    Cart.objects.create(user=user,product=item.product, product_qty=1)  #if not in cart, create cart item
                    
                    item.delete()    #Remove item from wishlist
            
            return redirect('cart')        
        
        else:
            
            return JsonResponse({"status":"User not logged in"})  
        
    return redirect('/')      
                        
                       