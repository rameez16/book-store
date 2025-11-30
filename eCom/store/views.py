from django.shortcuts import render,redirect

from . models import *

from django.contrib import messages

# Create your views here.


def home(request):
    
    trending_books=ProductItem.objects.filter(trending='yes')
    
    context={'trending_books':trending_books}
    
    return render(request,"store/home.html",context)



def collections(request):
    
    category=Category.objects.filter(status=0)
    
    context={"category":category}
    
    return render(request,"store/collections.html",context) 
    



def collectionsview(request,slug):
    
    if(Category.objects.filter(slug=slug,status=0)):
        products=ProductItem.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={'products':products,'category':category}
        return render(request,"store/products/home.html",context)
    
    else:
        messages.warning(request,"No such category found")
        return redirect('collections')
        
        
        
def productview(request,cat_slug,pro_slug):
    
    
    product_details=ProductItem.objects.filter(slug=pro_slug).first()
    
    context={'product':product_details}
    
    
    return render(request,'store/products/product_details.html',context)


        
    


       