from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Purchase
from .forms import PurchaseForm

def index(request):
    return HttpResponse("This is the index")

def purchases_list(request):
    purchases = Purchase.objects.all()

    return render(request, 'shared_list/purchases_list.html', {'purchases': purchases})

def new_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            product_price = form.cleaned_data['product_price']
            p = Purchase(product_name = product_name, product_price = product_price)
            p.save()
            return HttpResponseRedirect('../../shared_list')

    else:
        form = PurchaseForm()

    return render(request, 'shared_list/new_purchase.html', {'form': form})