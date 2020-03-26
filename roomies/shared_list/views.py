from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Purchase, SharedList
from .forms import PurchaseForm,PurchasesListForm

def index(request):
    return HttpResponse("This is the index")

def purchases_list(request):

    try:
        sl = SharedList.objects.get(user=request.user)
    except SharedList.DoesNotExist:
        sl = None

    if sl is not None:
        purchases = Purchase.objects.filter(shared_list=sl)
        if len(purchases) > 0:
            return render(request, 'shared_list/purchases_list.html', {'purchases': purchases, 'sharedlist':True})
        else:
            return render(request, 'shared_list/purchases_list.html', {'purchases': None,'sharedlist': True})
    else:
        return render(request, 'shared_list/purchases_list.html', {'sharedlist': False})

def new_purchases_list(request):
    if request.method == 'POST':
        form = PurchasesListForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            pl = SharedList(name=name, user=request.user)
            pl.save()
            return HttpResponseRedirect('../../shared_list')

    else:
        form = PurchasesListForm()

    return render(request, 'shared_list/new_purchases_list.html', {'form': form})

def new_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            product_price = form.cleaned_data['product_price']
            user = request.user
            sl = SharedList.objects.get(user=user)
            p = Purchase(user=user, shared_list=sl, product_name=product_name, product_price=product_price)
            p.save()

            return HttpResponseRedirect('../../shared_list')

    else:
        form = PurchaseForm()

    return render(request, 'shared_list/new_purchase.html', {'form': form})