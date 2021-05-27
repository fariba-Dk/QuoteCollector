from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Quote, Category
from .forms import QuoteForm, CategoryForm



#RANDOM Quote
quotes_arr=["'If life were predictable it would cease to be life and be without flavor.' -Eleanor Roosevelt",
'"In the end, it\'s not the years in your life that count. It\'s the life in your years." -Abraham Lincoln',
'"Life is a succession of lessons which must be lived to be understood." -Ralph Waldo Emerson',
'"You will face many defeats in life, but never let yourself be defeated." -Maya Angelou',
'"Never let the fear of striking out keep you from playing the game." -Babe Ruth',
'"Life is never fair, and perhaps it is a good thing for most of us that it is not." -Oscar Wilde',
'"The only impossible journey is the one you never begin." -Tony Robbins',
'"In this life we cannot do great things. We can only do small things with great love." -Mother Teresa',
'"Only a life lived for others is a life worthwhile." -Albert Einstein',
'"The purpose of our lives is to be happy." -Dalai Lama',
'"Life is what happens when you\'re busy making other plans." -John Lennon',
'"You only live once, but if you do it right, once is enough." -Mae West',
'"Live in the sunshine, swim the sea, drink the wild air." -Ralph Waldo Emerson',
'"Go confidently in the direction of your dreams! Live the life you\'ve imagined." -Henry David Thoreau',
'"The greatest glory in living lies not in never falling, but in rising every time we fall." -Nelson Mandela',
'"Life is really simple, but we insist on making it complicated." -Confucius',
'"May you live all the days of your life." -Jonathan Swift',
'"Life itself is the most wonderful fairy tale." -Hans Christian Andersen',
'"Do not let making a living prevent you from making a life." -John Wooden',
'"Life is ours to be spent, not to be saved." -D. H. Lawrence',
'"Keep smiling, because life is a beautiful thing and there\'s so much to smile about." -Marilyn Monroe',
'"Life is a long lesson in humility." -James M. Barrie',
'"In three words I can sum up everything I\'ve learned about life: it goes on." -Robert Frost',
'"Love the life you live. Live the life you love." -Bob Marley',
'"Life is either a daring adventure or nothing at all." -Helen Keller',
'"You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose." -Dr. Seuss',
'"Life is made of ever so many partings welded together." -Charles Dickens',
'"Your time is limited, so don\'t waste it living someone else\'s life. Don\'t be trapped by dogma -- which is living with the results of other people\'s thinking." -Steve Jobs',
'"Life is trying things to see if they work." -Ray Bradbury',
'"Many of life\'s failures are people who did not realize how close they were to success when they gave up." -Thomas A. Edison'
],


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




