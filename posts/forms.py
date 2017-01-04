from django import forms

class ItemForm(forms.Form):
    name = forms.CharField(label='Item name', max_length=100)
    description = forms.CharField(label ='Description', max_length=300)
    form_price = forms.DecimalField(label='Price', max_digits=6, decimal_places=2)
    form_link = forms.CharField(label='Link to retail page', max_length=300)