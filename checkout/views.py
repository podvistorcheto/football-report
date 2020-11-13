from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import PackageForm
from cart.contexts import cart_contents
import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    cart = request.session.get('cart', {})
    if not cart:
        messages.warning(request, "The shopping cart is empty")
        return redirect(reverse('subscription'))

    current_cart = cart_contents(request)
    total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent =stripe.PaymentIntent.create(
        amount = stripe_total,
        currency = settings.STRIPE_CURRENCY,
    )

    print(intent)

    package_form = PackageForm()
    template = 'checkout/checkout.html'
    context = {
        'package_form': package_form,
        'stripe_public_key': 'pk_test_51HDOLVLVB4v4eSDr59suh8eAYNpAHN4UQpFkGC53RHABUiRlPOjjAtgzSfQIVfm5gTKOqGQGbFSRTKrJLCsXYxmQ00xgRmGPUa',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
