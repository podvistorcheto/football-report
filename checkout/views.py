from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import PackageForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "The shopping cart is empty")
        return redirect(reverse('subscription'))

    package_form = PackageForm()
    template = 'checkout/checkout.html'
    context = {
        'package_form': package_form,
    }

    return render(request, template, context)
