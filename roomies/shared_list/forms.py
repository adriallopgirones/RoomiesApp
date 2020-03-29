from django import forms

class PurchaseForm(forms.Form):
    product_name = forms.CharField(label='Product name', max_length=100)
    # product_price = forms.IntegerField(label='Product price')

class PurchasesListForm(forms.Form):
    name = forms.CharField(label='list name', max_length=100)

class PayPurchaseForm(forms.Form):
    price = forms.FloatField(label='How much did it cost to you?')