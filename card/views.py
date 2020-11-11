from django.shortcuts import render

# Create your views here.

def view_card(request):
    """ a method that renders the card contents page"""

    return render(request, 'card/card.html')