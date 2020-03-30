from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template.response import TemplateResponse
from .models import Purchase, SharedList
from .forms import PurchaseForm, PayPurchaseForm
from django.contrib.auth import get_user_model
from django.apps import apps
import GroupManagerInstance

def index(request):
    return HttpResponse("This is the index")

def purchases_list(request):

    try:
        sl = SharedList.objects.get(group_id=request.user.group_id)
        update_group_manager(request)

    except SharedList.DoesNotExist:
        sl = None

    User = get_user_model()
    user = User.objects.get(username=request.user)

    if user.is_grouped:
        table = GroupManagerInstance.GM.build_debts_table()
        purchases = Purchase.objects.filter(shared_list=sl)
        if len(purchases) > 0:
            return render(request, 'shared_list/purchases_list.html', {'purchases': purchases, 'sharedlist':True,
                                                                       'debts_table' : table})
        else:
            return render(request, 'shared_list/purchases_list.html', {'purchases': None, 'sharedlist': True,
                                                                       'debts_table' : table})
    else:
        return render(request, 'shared_list/purchases_list.html', {'sharedlist': False})

def new_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            product_name = form.cleaned_data['product_name']
            user = request.user
            sl = SharedList.objects.get(group_id=user.group_id)
            p = Purchase(user=user, shared_list=sl, product_name=product_name)
            p.save()

            return HttpResponseRedirect('../../shared_list')

    else:
        form = PurchaseForm()

    update_group_manager(request)

    return render(request, 'shared_list/new_purchase.html', {'form': form})

def delete_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)

    if request.method == 'POST':
        purchase.delete()
        return HttpResponseRedirect('../../')

    update_group_manager(request)

    return HttpResponseRedirect('../../')

def pay_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        form = PayPurchaseForm(request.POST, user=request.user)
        if form.is_valid():
            User = get_user_model()
            price = form.cleaned_data['price']
            payer = form.cleaned_data['payer']
            receivers = form.cleaned_data['receivers']
            receivers = repr([str(r.username) for r in receivers])
            purchase.user = User.objects.get(username = payer)
            purchase.receivers = receivers
            purchase.purchased = True
            purchase.product_price = price
            purchase.save()
            update_group_manager(request)
            debts_table = GroupManagerInstance.GM.update_debts()
            users = User.objects.filter(group_id=request.user.group_id)

            for user in users:
                user.debt = debts_table[user.username]
                user.save()

            return HttpResponseRedirect('../../')

    else:
        form = PayPurchaseForm(user=request.user)

    return render(request, 'shared_list/pay_purchase.html', {'form': form, 'purchase_id': purchase.id})


def update_group_manager(request):
    User = get_user_model()
    user = User.objects.get(username=request.user)
    users = User.objects.filter(group_id=user.group_id)
    Purchase = apps.get_model('shared_list', 'Purchase')
    SharedList = apps.get_model('shared_list', 'SharedList')
    purchases = Purchase.objects.filter(shared_list=SharedList.objects.get(group_id=user.group_id))
    GroupManagerInstance.GM.update_group(users, purchases, user.group_id)