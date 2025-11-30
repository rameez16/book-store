superuser username-admin
superuser password-admin





steps to start a django project
__________________________

1. Create a  project folder and open with vs code
2. Create virtual environment inside the project folder : in ternmial type cmd-->  python -m venv venv
3. Activate the virtual envirnment  cmd:--> venv\Scripts\activate 
3. install django  cmd:--> pip install django ( chek in venv library ) 

# create project -  >  django-admin startproject myproject

5. run python manage.py runserver


# create  an app named store     -  >  python manage.py startapp store

6.register the app in settings.py

7.in project folder find url.py, add app urls here.

8.in app folder create url.py->add url to find home function inside views.py

9.inside the views.py write function named home to return home.html file inside templates directory

10.create template dir in app.inside template dir . create store diretcory.here create home.html 

11.inside home.html create html file to render in home route ''.





products=ProductItem.objects.filter(category__slug=slug)
Breakdown:
ProductItem.objects: Accesses the ProductItem model manager

.filter(): Database query method to get matching records

category__slug=slug: This uses Django's foreign key lookup syntax

category is likely a ForeignKey field in ProductItem that points to Category model

__slug (double underscore) means "look up the slug field on the related Category object"

So it's filtering: "Get all ProductItems where the related Category's slug equals the given slug parameter"







✅ Why item.category.slug Works in Django
✔️ 1. You are looping through products

So each item is a Product object.

✔️ 2. A Product has a ForeignKey to Category

Your Product model probably looks like:

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # ... other fields like name, slug, price, etc.


This means every Product has a category object attached to it.

So when you write:

item.category


You get the Category object linked to the product.





<!-- <a href="{% url 'productview' item.category.slug item.slug %}"> -->
This means:

The URL pattern for productview expects two parameters:

category slug

product slug

Example:

bash
Copy code
/electronics/iphone-14/
So the URL tag fills them in:

item.category.slug → "electronics"

item.slug → "iphone-14"

🧠 So your understanding is correct:
Product (item) does not have its own category slug field → but it does have a relationship to category.

Category does have a slug, so we access it using item.category.slug.

Django automatically joins the two models internally when accessing related field






Your Product View Code (Explained Line by Line)

Your code:

def productview(request, cate_slug, prod_slug):
    if Category.objects.filter(slug=cate_slug, status=0).exists():
        if Product.objects.filter(slug=prod_slug, status=0).exists():
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products' : products}
        else:
            messages.error(request,"no such product found!")
            return redirect('collections')
    else:
        messages.error(request,"no such category found")
        return redirect('collections')
    return render(request,"store/products/view.html",context)

🟦 1. Function receives two slugs from the URL

Your URL probably looks like:

path('collections/<str:cate_slug>/<str:prod_slug>/', views.productview)


So Django sends:

cate_slug → category slug from the URL

prod_slug → product slug from the URL

Example URL:

/collections/electronics/iphone-14/


So the function receives:

cate_slug = "electronics"
prod_slug = "iphone-14"

🟦 2. Check if category exists
if Category.objects.filter(slug=cate_slug, status=0).exists():


This checks:

Is there a category with this slug?

Is status = 0 (means active category)

If NOT found → redirect with error message.

🟦 3. If category exists, check for the product
if Product.objects.filter(slug=prod_slug, status=0).exists():


This checks:

Is there a product with this slug?

Is the product active?

If product NOT found → redirect with "no such product found".

🟦 4. If product exists → fetch it
products = Product.objects.filter(slug=prod_slug, status=0).first()


You are fetching the first matching product.

A better way would be .get(), but your code works fine.

🟦 5. Pass product to template
context = {'products': products}
return render(request,"store/products/view.html", context)


This sends the product data to:

store/products/view.html


So inside the template, you can write:

{{ products.name }}
{{ products.price }}
{{ products.product_image.url }}

🔵 🧠 Overall Flow (Simple Explanation)

User clicks product

URL passes category slug + product slug

Django verifies category exists

Django verifies product exists

Django loads product

Django sends product info to template

Template shows the product page




Authentication
________________________________



✅ Django Form Cycle (VERY IMPORTANT)
1️⃣ User visits /register → GET request

Django calls register() (first time)

request.method == 'GET'

Django shows empty form

return render(request, "register.html", {"form": empty_form})


2️⃣ User submits the form → POST request

Browser sends a new request

Django calls register() again

This time: request.method == 'POST'

Django validates submitted data

If valid → save → redirect
If NOT valid → show form with errors



User: opens /register
        │
        ▼
Django: GET /register
        │
        ▼
Show empty form
        │
        ▼
User fills form & clicks Submit
        │
        ▼
Browser sends POST /register
        │
        ▼
Django: POST /register
        │
        ├── valid? → save → redirect('/login')
        │
        └── invalid? → show form with errors (same template)




CustomUserForm
      │
      ▼
inherits → UserCreationForm
      │
      ├── built-in validation (password check)
      ├── hashing logic
      ├── save() implementation
      │
      ▼
Your custom fields change:
      - placeholder
      - HTML styling
      - widget type
      (UI only)
      │
      ▼
Meta class:
      tells Django → use User model + these 4 fields
      │
      ▼
form.save() creates new User


