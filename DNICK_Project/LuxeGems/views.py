from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from LuxeGems.forms import RegistryForm, LoginForm, JewelryForm, PaymentForm
from LuxeGems.models import Jewelry, Registry


# Create your views here.

def calculate_total_price(cart):
    total = 0

    for jewelry_id, item in cart.items():
        if 'price' in item:
            quantity = item.get('quantity', 0)
            price = item.get('price', 0)
            item_total = quantity * price
            total += item_total
    return total

def home(request):
    jewelry = Jewelry.objects.all()[:2]
    context = {"jewelry": jewelry}
    return render(request, "home.html", context=context)


def card(request):
    jewelry = Jewelry.objects.all()[:2]
    context = {"jewelry": jewelry}
    return render(request, "card.html", context=context)


def rings(request):
    jewelry = Jewelry.objects.filter(category="Прстен").all()
    context = {"jewelry": jewelry}
    return render(request, "rings.html", context=context)


def detail(request, jewelry_id):
    jewelry = Jewelry.objects.get(id=jewelry_id)
    context = {"jewelry": jewelry}
    return render(request, "jewelleryDetail.html", context=context)


def bracelets(request):
    jewelry = Jewelry.objects.filter(category="Белегзија").all()
    context = {"jewelry": jewelry}
    return render(request, "bracelets.html", context=context)


def watches(request):
    jewelry = Jewelry.objects.filter(category="Часовник").all()
    context = {"jewelry": jewelry}
    return render(request, "watches.html", context=context)


def charms(request):
    jewelry = Jewelry.objects.filter(category="Приврзок").all()
    context = {"jewelry": jewelry}
    return render(request, "charms.html", context=context)


def earrings(request):
    jewelry = Jewelry.objects.filter(category="Обетки").all()
    context = {"jewelry": jewelry}
    return render(request, "earrings.html", context=context)


def thanks(request):
    cart = request.session.get('cart', {})
    total = calculate_total_price(cart)

    request.session['cart'] = {}

    request.session.save()

    context = {"total": total}
    return render(request, "thanks.html", context=context)


def add(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("You are not authorized to access this page.")
    form = JewelryForm(request.POST or None, request.FILES or None)
    # print(form)
    if form.is_valid():
        if request.method == "POST":
            form = JewelryForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                jewelry = form.save(commit=False)
                jewelry.user = request.user
                jewelry.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'add.html', context)


def registry(request):
    form = RegistryForm(request.POST or None)

    if form.is_valid():
        if request.method == "POST":
            form = RegistryForm(request.POST)
            if form.is_valid():
                fly = form.save(commit=False)
                fly.user = request.user
                fly.save()
        return redirect('login')

    context = {'form': form}
    return render(request, 'registry.html', context)


def payment(request):
    form = PaymentForm(request.POST or None)

    cart = request.session.get('cart', {})
    total = calculate_total_price(cart)

    if form.is_valid():
        if request.method == "POST":
            form = PaymentForm(request.POST or None)
            if form.is_valid():
                pay = form.save(commit=False)
                pay.sum_price = total
                pay.save()
        return redirect('thanks')

    context = {'form': form}
    return render(request, 'payment.html', context)


def login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        # print(username)
        password = form.cleaned_data['password']
        # print(password)
        user = Registry.objects.filter(username=username).first()
        # print(user)

        if user is not None and password == user.password:
            log = form.save(commit=False)
            log.user = request.user
            log.save()
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    context = {'form': form}
    return render(request, 'login.html', context)


def card(request):

    cart = request.session.get('cart', {})
    total = calculate_total_price(cart)

    return render(request, 'card.html', {'cart': cart, 'total': total})


def add_to_cart(request, jewelry_id):
    jewelry = get_object_or_404(Jewelry, pk=jewelry_id)

    cart = request.session.get('cart', {})

    cart_item = cart.get(str(jewelry_id), {'quantity': 0, 'name': '', 'price': 0})
    cart_item['quantity'] += 1
    cart_item['name'] = jewelry.name
    cart_item['price'] = jewelry.price

    cart[str(jewelry_id)] = cart_item

    request.session['cart'] = cart
    # print(cart)
    return redirect('card')


def delete_cart(request):
    request.session['cart'] = {}
    request.session.save()

    return redirect('card')
