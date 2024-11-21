from django.urls import path
from .import views
urlpatterns = [
    path('about.html', views.about,name = 'about.html'),
    path('contact.html', views.contact,name = 'contact'),
    path('faq.html', views.faq,name = 'faq.html'),
    path('index.html', views.index,name = 'index.html'),
    path('product-detail.html', views.product_detail,name = 'product-detail.html'),
    path('products.html', views.products,name = 'products.html'),
    path('sign-in.html', views.sign_in,name = 'sign-in.html'),
    path('sign-up.html', views.sign_up,name = 'sign-up.html')
]