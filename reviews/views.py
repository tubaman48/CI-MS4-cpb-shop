""" Views for reviews app """

from django.shortcuts import render
from django.db.models.functions import Lower
from .models import Review


def all_reviews(request):
    """The view to show all reviews and sorting functionality"""

    reviews = Review.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'username':
                sortkey = 'username__username'
                reviews = reviews.annotate(
                    lower_username=Lower('username__username'))
            if sortkey == 'product':
                sortkey = 'product__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            reviews = reviews.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'reviews': reviews,
        'current_sorting': current_sorting,
    }

    return render(request, 'reviews/reviews.html', context)
