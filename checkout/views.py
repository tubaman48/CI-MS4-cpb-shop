""" checkout views """

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """ checkout function """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JxJDkIDOPonb4zrNOMUfJfDuJJW3hld3DSsUvV'
        '0cqsUzLpnYZV8yuuTxthyC61uVtbrHQchutGwj3B6VIJkbUhZ00IKqaQknq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
