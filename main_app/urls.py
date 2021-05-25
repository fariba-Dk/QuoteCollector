from django.urls import path
from . import views

urlpatterns =[
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('quotes/', views.index, name='index'),
  path('reviews/', views.reviews, name='reviews'),
  path('quotes/new/', views.create_quote, name='create_quote')
]
