from django.shortcuts import render
from reviews.models import Review
# Create your views here.

def index(request):
    """ View to return the index page with reviews """

    review = Review.objects.order_by('-date_created')
    context = {
        'review': review
    }
    return render(request, 'home/index.html', context)

