from django.shortcuts import render
from reviews.models import Review
# Create your views here.

def index(request):
    """ View to return the index page """
    return render(request, 'home/index.html')


def reviews_carousel(request):
    """ A view to return the reviews to carousel """
    review = Review.objects.order_by('-date_created')
    context = {
        'review': review
    }
    return render(request, template, context)

