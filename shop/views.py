from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm

# Create your views here.


def index(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product':product})


def women(request):
    product = Women.objects.all()
    return render(request, 'women.html', {'product': product})


def men(request):
    product = Men.objects.all()
    return render(request, 'men.html', {'product': product})


# def men(request):
#     products = Men.objects.all()
#     return render(request, 'index.html', {'products': products})


def productView(request, myid):
    # Fetch the product using the id
    product = get_object_or_404(Product, id=myid,  available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'prodView.html', {'product': product, 'cart_product_form': cart_product_form})

    # return render(request, 'prodView.html', {'product':product[0]})


def menView(request, id):
    # Fetch the product using the id
    prod = get_object_or_404(Men, id=id,  available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'menView.html', {'prod': prod, 'cart_product_form': cart_product_form})


def womenView(request, myid):
    # Fetch the product using the id
    # product = Women.objects.filter(id=id)
    product = get_object_or_404(Women, id=myid, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'womenView.html', {'product': product, 'cart_product_form': cart_product_form})

    # return render(request, 'womenView.html', {'product':product[0]})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# def blog(request):
#     return render(request, 'blog.html')

def blog(request):
    fetch_data = Blog.objects.all()
    return render(request, 'blog.html', {'data':fetch_data})


def blog_single(request, id):
    if request.POST:
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']

        query = Comment(message=message, name=name, email=email)
        query.post_id_id = id
        query.save()

    data = Blog.objects.get(id=id)
    comment = Comment.objects.all().filter(post_id=id)
    return render(request, 'blog-single.html', {'data':data, 'comment':comment})


def brand(request):
    return render(request, 'our_brand.html')


def founder(request):
    return render(request, 'our_founder.html')


def women_content(request):
    return render(request, 'women-content.html')


def men_clothing(request):
    return render(request, 'men-clothing.html')
