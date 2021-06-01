from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quote, Category
from .forms import QuoteForm, CategoryForm


# class Quote:
#   def __init__(self, theme, author, content, date):
#     self.theme = theme
#     self.author = author
#     self.content = content
#     self.date = date

quotesArr = []

#HOME PAGE
def home(request):
  context = {'quotesArr': quotesArr }

  return render(request, 'home.html',context)

#ABOUT
def about(request):
  context = {'quotesArr': quotesArr }


  return render(request, 'about.html', context)

#REVIEW QUOTE
def reviews(request):
  return render(request, 'reviews.html')

#INDEX QUOTES
def index(request):
  quote = Quote.objects.all()
  print(quote)

  #template
  context = { 'quotes': quote }
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
    form = QuoteForm(request.POST, instance=quote)
    if form.is_valid():
      quote = form.save()
      return redirect('detail', quote_id)



#ADD category to quote
def assoc_category(request, quote_id, category_id):
  found_quote = Quote.objects.get(id=quote_id)
  found_quote.category.add(category_id)
  return redirect('detail', quote_id)




