from django.db import models

# Create your models here.
class Quote:
  def _init_(self, quote_type, description, date):
    self.quote_type = quote_type
    self.description = description
    self.data = date
