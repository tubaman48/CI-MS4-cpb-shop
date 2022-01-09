""" Views for reviews app """

from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm


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


@login_required
def add_review(request):
    """The view to add a review to the site"""

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.username = request.user
            review.save()
            messages.success(request, 'You added a new review!')
            return redirect(
                reverse('reviews')
                )

        else:
            messages.error(
                request, 'This review was not added. ' +
                'Please check the form is valid.'
                )
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
