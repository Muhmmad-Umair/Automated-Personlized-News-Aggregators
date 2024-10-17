from django import forms
from django.forms import ModelForm
from .models import News, NewsCategory

class NewsForm(forms.ModelForm):
  class Meta:
    model = News
    fields = '__all__'