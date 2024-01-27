from django import forms

class BookQueryForm(forms.Form):
     query = forms.CharField(label='Query', max_length=100)