from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('how_it_works/', views.how_it_works, name='how_it_works'),
    path('legal/', views.legal, name='legal'),
    path('terms/', views.terms, name='terms'),
    path('services/', views.services, name='services'),
    path('services_details/', views.services_detail, name='services_detail'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
