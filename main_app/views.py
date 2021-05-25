from django.shortcuts import render
from django.http import HttpResponse
from .models import Quote
import json
from .forms import QuoteForm


class Quote:
  def _init_(self, quote_type, description, date):
    self.quote_type = quote_type
    self.description = description
    self.data = date

# Create your views here.
def home(request):
  return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


def index(request):
  context = { 'quotes': quotes }
  #retrieve a template and send HTML back
  return render(request, 'quotes/quotes_index.html', context)


#REVIEW QUOTE
def reviews(request):
  return render(request, 'reviews.html')


#CREATE QUOTE
def create_quote(request):
  if request.method == 'GET':
    form = QuoteForm()
    context = {
      'form': form
    }
    return render(request,'quotes/quotes_new.html', context)

