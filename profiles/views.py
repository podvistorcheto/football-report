from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """ to display user's profile page """
    profile = get_object_or_404(Profile, user=request.user)
    order = get_object_or_404(Package, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = "profiles/profile.html"
    context = {
        'profile': profiles,
        'order': order,
        'from_profile': True,
    }
    
    return render(request, template, context)