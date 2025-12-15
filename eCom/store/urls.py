from django.urls import path

from . import views 

from store.controller import authview,cart,checkout,orders,wishlist


urlpatterns = [
    path('',views.home,name='home'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:slug>',views.collectionsview,name='collectionsview'),
    path('collections/<str:cat_slug>/<str:pro_slug>',views.productview,name='productview'),
   
    path('register',authview.register,name='register'),
    path('login/',authview.login_page,name="login"),
    path('logout/',authview.logout_page,name='logout'),
    
    path('cart',cart.cartview,name='cart'),
    path('add-to-cart',cart.addtocart,name='add-to-cart'),
    path('update-cart',cart.updatecart,name='update-cart'),
    path('delete-cart-item',cart.delete_cart_item,name='delete-cart-item'),
    
    path('wishlist',wishlist.index,name='wishlist'),
    path('add-to-wishlist',wishlist.add_to_wishlist,name='add-to-wishlist'),
    path('move-to-cart',wishlist.move_item_to_cart_from_wishlist,name='move-to-cart'),
    
     path('checkout/',checkout.index,name='checkout'),
     path('place-order',checkout.place_order,name="placeorder"),
     path('proceed-to-pay/',checkout.razorpay_check,name='proceed-to-pay'),
     
     path('order/',orders.order,name='order')
   
]


