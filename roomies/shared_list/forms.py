from django import forms
from django_select2.forms import Select2MultipleWidget
from django.contrib.auth import get_user_model

class PurchaseForm(forms.Form):
    product_name = forms.CharField(label='Product name', max_length=100)
    # product_price = forms.IntegerField(label='Product price')

class PurchasesListForm(forms.Form):
    name = forms.CharField(label='list name', max_length=100)

class EditPurchaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        print(kwargs)
        user = kwargs.pop('user')
        super(EditPurchaseForm, self).__init__(*args, **kwargs)
        self.fields['receivers'] = forms.ModelMultipleChoiceField(
            label='Who are the receivers?',
            queryset=get_user_model().objects.filter(group_id = user.group_id),
            widget=Select2MultipleWidget)
        self.fields['payer'] = forms.ChoiceField(choices = [(u.username, u.username) for u in (get_user_model().objects.filter(group_id = user.group_id))])
    price = forms.FloatField(label='How much did it cost to you?')