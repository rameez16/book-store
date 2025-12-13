
from django.shortcuts import redirect,render
from django.contrib import messages
import random

from django.http.response import JsonResponse
from store.models import ProductItem,Cart,User,Profile,Order,OrderItem


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
    



def place_order(request):
    
        if request.method=='POST':
            
            current_user=User.objects.filter(id=request.user.id).first()
            
            if not current_user.first_name:
                current_user.first_name=request.POST.get('firstname')
                current_user.last_name=request.POST.get('lastname')
                current_user.save()
            
        if not Profile.objects.filter(user=request.user):
            userprofile=Profile()
            userprofile.user=request.user
            userprofile.phone=request.POST.get('Phone')
            userprofile.address=request.POST.get('Address')
            userprofile.city=request.POST.get('City')
            userprofile.state=request.POST.get('State')
            userprofile.country=request.POST.get('Country')
            userprofile.pincode=request.POST.get('PinCode')
            userprofile.save()
            
        new_order=Order()
        new_order.user=request.user
        new_order.fname=request.POST.get('firstname')
        new_order.lname=request.POST.get('lastname')
        new_order.email=request.POST.get('email')
        new_order.phone=request.POST.get('Phone')
        new_order.address=request.POST.get('Address')
        new_order.city=request.POST.get('City')                
        new_order.country=request.POST.get('State')
        new_order.country=request.POST.get('Country')
        new_order.pincode=request.POST.get('PinCode')


        new_order.payment_mode=request.POST.get('payment_mode')
        new_order.payment_id=request.POST.get('payment_mode')


        cart=Cart.objects.filter(user=request.user)
        cart_total_price=sum( item.product.selling_price*item.product_qty for item in cart)
        new_order.total_price=cart_total_price
        tracking_no='Amrita'+str(random.randint(11111111,99999999))
        
        
        while Order.objects.filter(tracking_no=tracking_no).exists():
            tracking_no='Amrita'+str(random.randint(11111111,99999999))
        
        new_order.tracking_no=tracking_no
        new_order.save()
        
        
        for item in cart:
           
           OrderItem.objects.create(
               order=new_order,product=item.product,price=item.product.selling_price,quantity=item.product_qty
           )
           
           if ProductItem.objects.filter(id=item.product.id).exists():
               
               ordered_product= ProductItem.objects.filter(id=item.product.id).first()
               ordered_product.quantity-=item.product_qty
               ordered_product.save()
        
        Cart.objects.filter(user=request.user).delete()
        
        messages.success(request,"Your order has been successfully completed")
        
        payMode =request.POST.get("payment_mode")
        
        if payMode == 'Paid by Razorpay' :
            
            return JsonResponse({'status':"Your order has been placed successfully "})
        
        return redirect('order/')
            
def razorpay_check(request):
    
    cart=Cart.objects.filter(user=request.user)
    total_price=0
    
    for item in cart:
        total_price+=(item.product.selling_price*item.product_qty)
    return JsonResponse({"total_price":total_price})
    
    
                        
        
              
               
               
                 
            
            
            
            
            
            
            
    
    