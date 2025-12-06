
from django.shortcuts import redirect,render
from django.contrib import messages

from django.http.response import JsonResponse

from store.models import ProductItem,Cart,User


def addtocart(request):
    
    if request.method=='POST':
        
        if request.user.is_authenticated:
            
            product_id=int(request.POST.get('product_id'))
            
            product= ProductItem.objects.get(id=product_id)
            
            if(product):
                
                if(Cart.objects.filter(product_id=product_id)):  
                    
                    # cart=Cart.objects.filter(user=request.user)   
                    # cart_data = [{'product_id': item.product_id, 'product_name': item.product_id.name, 'quantity': item.product_qty} for item in cart]          
                    return JsonResponse({'status': 'Product already inside the cart' })
                
                
                else:
                    
                    quantity=int(request.POST.get('product_qty'))
                    
                    if(product.quantity>=quantity):
                        
                        Cart.objects.create(user=request.user,product=product,product_qty=quantity)
                   
                        return JsonResponse({'status':'Product added to cart'})
                    
                    else:
                        
                        return JsonResponse({'status' : 'insufficient quantity'})  
                    
            else:
               
               return JsonResponse({'status' : 'Product not available'})
        else:
            
            return JsonResponse({'status':'User not Authenticated','message': 'Please login to add items to cart',
                    'redirect_url': '/login/'}, status=401)
                      
    
    return redirect('/')




def cartview(request):
    
    
     user=request.user
     
     if user.is_authenticated :
         
         cart_items=Cart.objects.filter(user=user)
     
     else:
         
         cart_items=[]
         redirect ('/login')       
           
                  
     context={'cart_items':cart_items,}
    
     return  render(request,'store/cart.html',context)   
    
    


