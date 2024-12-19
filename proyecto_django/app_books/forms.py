from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'valuation']


    def clean_valuation(self):
        valuation = self.cleaned_data.get('valuation')
        if valuation > 10000 or valuation < 0:
            raise forms.ValidationError('La valoración debe estar entre 0 y 10000.')
        return valuation