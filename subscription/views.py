from django.shortcuts import render
from subscription.models import Subscription


# view for donation page
def subscriptions(request):
    '''
    function to get all donation objects in db
    and pass to template for display
    '''
    subscriptions = Subscription.objects.all()
    context = {
        "subscriptions": subscriptions,
        "title": 'Subscriptions'
    }
    return render(request, 'subscription/subscription.html', context)
