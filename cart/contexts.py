from django.shortcuts import get_object_or_404
from django.conf import settings
from subscription.models import Subscription


def cart_contents(request):
    '''
    Ensures that the cart contents are available when rendering
    every page
    '''
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    subscription_count = 0
    """
    context = {
        'cart_items': cart_items,
        'total': total,
        'subscription_count': subscription_count,
    }"""

    for id, quantity in cart.items():
        subscription = get_object_or_404(Subscription, pk=id)
        total += quantity * subscription.price
        subscription_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'subscription': subscription})

    return {'cart_items': cart_items, 'total': total, 'suscription_count': subscription_count}
