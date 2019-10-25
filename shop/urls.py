from django.contrib import admin
from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:myid>', views.productView, name='ProductView'),
    # path('products/<int:myid>', views.productView, name='ProductView'),
    path('menView/<str:id>', views.menView, name='menView'),
    path('women/', views.women, name='women'),
    path('womenView/<int:myid>', views.womenView, name='womenView'),
    path('men/', views.men, name="men"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
    path('blog-single/<int:id>', views.blog_single, name="blog-single"),
    path('our-brand/', views.brand, name="brand"),
    path('our-founder/', views.founder, name="founder"),
    path('women-clothing/', views.women_content, name="women-content"),
    path('men-clothing/', views.men_clothing, name='men-clothing')

]
