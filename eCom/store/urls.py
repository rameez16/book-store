from django.urls import path

from . import views 

from store.controller import authview


urlpatterns = [
    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:slug>',views.collectionsview,name='collectionsview'),
    path('collections/<str:cat_slug>/<str:pro_slug>',views.productview,name='productview'),
   
    path('register',authview.register,name='register'),
    path('login/',authview.login_page,name="login"),
    path('logout/',authview.logout_page,name='logout')
]


