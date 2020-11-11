from django.conf import settings


def card_contents(request):
    
    card_items = []
    total = 0
    product_count = 0

    context = {
        'card_items': card_items,
        'total': total,
        'product_count': product_count,
    }

    return context
