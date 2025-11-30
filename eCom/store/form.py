from django.contrib.auth.forms import UserCreationForm

from . models import User





from django import forms

class CustomUserForm(UserCreationForm):
    
# ✔ This class inherits from Django's UserCreationForm.
# ✔ I override the form fields to add Bootstrap classes + placeholders.
    
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter Password1'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter Password1'}))
    
    class Meta:
        model=User
        fields=["username",'email','password1','password2']
  
        
# ✔ The Meta class tells Django:

# which model the form will save to

# which fields from that model should be used


# Meta Class in Simple Terms

# The Meta class tells Django:

# 1️⃣ Which database model the form is connected to
# model = User


# So Django knows:
# “When this form saves, create a User object.”





# CustomUserForm
#       │
#       ▼
# inherits → UserCreationForm
#       │
#       ├── built-in validation (password check)
#       ├── hashing logic
#       ├── save() implementation
#       │
#       ▼
# Your custom fields change:
#       - placeholder
#       - HTML styling
#       - widget type
#       (UI only)
#       │
#       ▼
# Meta class:
#       tells Django → use User model + these 4 fields
#       │
#       ▼
# form.save() creates new User

