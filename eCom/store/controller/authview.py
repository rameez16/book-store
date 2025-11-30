from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,render
from django.contrib import messages

from store.form import CustomUserForm


def register(request):
    
    form=CustomUserForm()   # empty form is  created   and
    
    if request.method=='POST':    # when user click submit form method become post 
        
        form=CustomUserForm(request.POST)  # filled the form with data 
        if form.is_valid():
            form.save()    # stored to database 
            messages.success(request,"registered successfully login to continue")
            return redirect('/login')   # redirected to login page.
    
    
    context={'form':form}      # passed as context  to template to render in UI      
                         
    return render(request,"store/auth/register.html",context)



# {
#     "username": "deepthi",
#     "email": "test@gmail.com",
#     "password1": "abc123",
#     "password2": "abc123"
# }


def login_page(request):
    
    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in")
        return redirect('/')
    else:
        if request.method=='POST':
            
            name=request.POST.get('Username')
            passwd=request.POST.get('Password')
            user=authenticate(request,username=name,password=passwd)
            
            
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            
            else:
                messages.error(request,"Invalid username & password")
                return redirect('/login')
            
            
    return render(request,"store/auth/login.html")        
            
            
def logout_page(request):
    
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged out Successfully")   
    return redirect('/')            