from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from subscription.models import Subscription


@login_required
def view_cart(request):
    '''a view that renders the cart contents page'''
    context = {
        'title': 'Cart'
    }
    return render(request, "cart/cart.html", context)


@login_required
def add_to_cart(request, id):
    ''' a method to add a subscription item to the cart'''
    subscription = Subscription.objects.get(pk=id)
    quantity = 1
    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)
    messages.success(request, f'Added {subscription.name} to your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


@login_required
def remove_from_cart(request, id):
    '''a method to remove subscription from the cart before checkout'''
    subscription = Subscription.objects.get(pk=id)
    item_id = id
    cart = request.session.get('cart', {})
    if cart[item_id] > 0:
        cart.pop(item_id)
        messages.warning(request, f'Removed {subscription.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
