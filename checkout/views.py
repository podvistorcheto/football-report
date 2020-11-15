from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from .forms import PackageForm
from .models import Package, PackageLineItem
from subscription.models import Subscription
from cart.contexts import cart_contents
from profiles.models import Profile

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }
        package_form = PackageForm(form_data)
        if package_form.is_valid():
            profile = Profile.objects.get(user=request.user)
            order = package_form.save(commit=False)
            order.user = profile
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            print(order)
            print(request.user)
            for item_id, item_data in cart.items():
                try:
                    subscription = Subscription.objects.get(id=item_id)
                    order.price = subscription.price
                    if isinstance(item_data, int):
                        package_line_item = PackageLineItem(
                            order=order,
                            subscription=subscription,
                            quantity=item_data,
                        )
                        package_line_item.save()
                        request.user.save()   
                except Subscription.DoesNotExist:
                    print(1)
                    messages.error(request, (
                        "Subscription wasn't found in our database. "
                        "Please contact us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            print(2)
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            print(3)
            messages.warning(request, "The shopping cart is empty")
            return redirect(reverse('subscription'))

        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount = stripe_total,
            currency = settings.STRIPE_CURRENCY,
        )

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment')

    package_form = PackageForm()
    template = 'checkout/checkout.html'
    context = {
        'package_form': package_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    print(4)
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    method for successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Package, order_number=order_number)
    messages.success(request, f'Payment successfully processed! \
        Your subscription number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    print(5)
    return render(request, template, context)
