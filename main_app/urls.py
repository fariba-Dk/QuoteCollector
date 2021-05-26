from django.urls import path
from . import views


urlpatterns =[
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('quotes/', views.index, name='index'),
  path('reviews/', views.reviews, name='reviews'),
  path('quotes/new/', views.create_quote, name='create_quote'),
  path('quotes/<int:quote_id>/', views.detail, name='detail'),
  path('quotes/<int:quote_id>/delete/', views.delete_quote, name='delete_quote'),
   path('quotes/<int:quote_id>/edit/', views.update_quote, name='update_quote'),
  path('quotes/<int:quote_id>/category/<int:category_id>/',views.assoc_category, name="assoc_category")
]

# Steps to create a new page
# 1. Create the path in urls.py
# 2. Create a view function
# 3. Create the template for the page
