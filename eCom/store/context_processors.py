from .models import *


def cart_count(request):
    
    user=request.user
    
    if user.is_authenticated:
        
        cart_count=Cart.objects.filter(user=user).count()
    else:
        
        cart_count=None    
        
    
    return {
        'cart_count':cart_count
    }    
        