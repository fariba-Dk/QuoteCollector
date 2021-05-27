from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quote, Category
from .forms import QuoteForm, CategoryForm



#RANDOM Quote
quotes_arr =[]


#HOME PAGE
def home(request):
  context = {'quotes_arr': quotes_arr }

  return render(request, 'home.html',context)

#ABOUT
def about(request):
  context = {'quotes_arr': quotes_arr }


  return render(request, 'about.html', context)

#REVIEW QUOTE
def reviews(request):
  return render(request, 'reviews.html')

#INDEX QUOTES
def index(request):
  quotes = Quote.objects.all()
  print(quotes)

  #template
  context = { 'quotes': quotes }
  #retrieve a template and send HTML back
  return render(request, 'quotes/quotes_index.html', context) #{'quotes':quotes

#DETAIL quotes
def detail(request, quote_id):

  found_quote = Quote.objects.get(id=quote_id)

  category_quote_doesnt_have = Category.objects.exclude(quote=quote_id)

  context ={
    'quote' : found_quote,
    'category': category_quote_doesnt_have
    }

  return render(request, 'quotes/quotes_detail.html', context)


#CREATE QUOTE
def create_quote(request):
  if request.method == 'GET':
    form = QuoteForm()
    context = {
      'form': form,
    }
    return render(request,'quotes/quotes_new.html', context)
  else:
      form = QuoteForm(request.POST)
      #QuoteForm to get data from request
      if form.is_valid():
        quote = form.save()
        return redirect('detail', quote.id) #or the detail page


#DELETE QUOTE
def delete_quote(request, quote_id):
  quote = Quote.objects.get(id=quote_id)
  quote.delete()
  return redirect('index')


#UPDATE QUOTE
def update_quote(request, quote_id):
  quote = Quote.objects.get(id=quote_id)

  if request.method == 'GET':
    form = QuoteForm(instance=quote)
    context = {
      'form': form,
    }
    return render(request,'quotes/quotes_edit.html', context)
  else:
    form = QuoteForm(request.POST, instace=quote)
    if form.is_valid():
      quote = form.save()
      return redirect('detail', quote_id)



#ADD category to quote
def assoc_category(request, quote_id, category_id):
  found_quote = Quote.objects.get(id=quote_id)
  found_quote.category.add(category_id)
  return redirect('detail', quote_id)




