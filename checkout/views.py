from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J81tDH0oItxg5aHT5Bv1EXoDQjtUIRo9NQ0avN9zjEtUNoVkemZjg7jBzhKAyzryHN0EN4W9sKPtts0VBSLolMb005s3NQRyY',
        'client_secret': 'test',
    }

    return render(request, template, context)