from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Profile
from checkout.models import Package


@login_required
def profile(request, order_number):
    """ to display user's profile page """
    profile = get_object_or_404(Profile, user=request.user)
    order = Package.objects.get.filter(instance=profile)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = "profiles/profile.html"
    context = {
        'profile': profile,
        'order': order,
        'from_profile': True,
    }
    
    return render(request, template, context)