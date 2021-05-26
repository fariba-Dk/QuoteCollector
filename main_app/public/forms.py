from django import forms
from .models import Quote
allbetter


class QuoteForm(forms.ModelForm):
  class Meta:
    model = Quote
    fields = ('content','description','date_added','theme')

