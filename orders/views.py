from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.forms import HiddenInput
from .models import MenuItem, OrderItem, Order
from .forms import OrderItemForm

# Create your views here.
def index(request):

    if not request.user.is_authenticated:
        return redirect('login')


    types  = MenuItem.objects.order_by().values_list('type', flat = True).distinct()

    type_dict = {}

    for type in types:
        values = {}

        names = MenuItem.objects.filter(type = type).values_list('name', flat = True).distinct()

        for name in names:
            values[name] = MenuItem.objects.filter(type = type, name = name)

        type_dict[type] = values

    context = {'types' : type_dict}

    return render(request, "orders/index.html", context)


def add(request, id):
    menuitem = MenuItem.objects.get(pk = id)

    order = Order.objects.filter(user = request.user, status = 'Open').first()

    if order is None:
        order = Order(user = request.user, status = 'Open')
        order.save()

    if request.method == 'POST':
        data = request.POST.copy()
        print(data)
        if 'toppings' in data and data['toppings'] == '':
            del data['toppings']
        if 'extras' in data and data['extras'] == '':
            del data['extras']
        form = OrderItemForm(data)
        print(form.data)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrderItemForm(initial = {'menuitem' : menuitem, 'order':order, 'toppings':None})

    form.fields['order'].widget = HiddenInput()
    form.fields['menuitem'].widget = HiddenInput()

    if menuitem.num_toppings == 0:
        form.fields['toppings'].widget = HiddenInput()

    available_items = menuitem.extra_set
    if available_items.count() == 0:
        form.fields['extras'].widget = HiddenInput()
    else:
        form.fields['extras'].queryset = available_items.all()

    context = {'menuitem' : menuitem,
    'form':form}
    return render(request, "orders/add.html", context)

def remove(request, id):
    OrderItem.objects.get(id=id).delete()
    return redirect('cart')

def cancel(request, id):
    order = Order.objects.get(id=id)
    order.status = 'Canceled'
    order.save()
    return redirect('orderlist')


def place(place, id):
    order = Order.objects.get(id=id)
    orderitems_no = order.orderitem_set.count()
    if orderitems_no == 0:
        return redirect('cart')
    order.status = 'Pending'
    order.save()
    return redirect('index')

def cart(request):
    order = Order.objects.filter(user = request.user, status = 'Open').first()

    if order is None:
        order = Order(user = request.user, status = 'Open')
        order.save()

    orderitems = order.orderitem_set.all()
    context = {'order' : order, 'orderitems':orderitems}
    return render(request, "orders/cart.html", context)


def orderlist(request):
    pending_orders = Order.objects.filter(user = request.user, status = 'Pending').all()

    completed_orders = Order.objects.filter(user = request.user, status = 'Completed').all()

    canceled_orders = Order.objects.filter(user = request.user, status = 'Canceled').all()

    context = {'pending_orders' : pending_orders, 'completed_orders' : completed_orders, 'canceled_orders' : canceled_orders}
    return render(request, "orders/orderlist.html", context)
