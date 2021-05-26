from django import forms
from .models import Quote, Category

class QuoteForm(forms.ModelForm):
  class Meta:
    model = Quote
    fields = ('theme','author','content','date')

class CategoryForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ('choices',)

