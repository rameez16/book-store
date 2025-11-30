from django.db import models
import datetime
import os
from django.contrib.auth.models import User
# Create your models here.

def get_file_path(request,filename):
    
    original_filename=filename
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    filename='%s%s' %(nowTime,original_filename)    
    return os.path.join('uploads/',filename)


class Category(models.Model):
    
    slug =models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    image =models.ImageField(upload_to=get_file_path,null=False,blank=False)
    description=models.TextField(max_length=375,null=False,blank=False)
    status=models.BooleanField(default=False,help_text='0=default,1-Hidden')
    trending=models.CharField(max_length=20,blank=False,null=False)
    meta_title=models.CharField(max_length=10,null=False,blank=False)
    meta_keyword=models.CharField(max_length=15,null=False,blank=False)
    meta_description=models.TextField(max_length=320,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    

    

class ProductItem(models.Model):
    
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True, blank=True)
    slug =models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)    
    product_image=models.ImageField(upload_to=get_file_path,null=False,blank=False)
    small_description=models.TextField(max_length=575,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    description=models.TextField(max_length=2150,null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    trending=models.CharField(max_length=20,blank=False,null=False)
    tag=models.CharField(max_length=25,blank=False,null=False)
    
    
    status=models.BooleanField(default=False,help_text='0=default,1-Hidden')
    meta_title=models.CharField(max_length=10,null=False,blank=False)
    meta_keyword=models.CharField(max_length=15,null=False,blank=False)
    meta_description=models.TextField(max_length=320,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    
    
    
    
    