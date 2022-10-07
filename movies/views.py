from django.shortcuts import redirect, render
from .forms import ReviewForm
from .models import Review

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews' : reviews,
    }
    return render(request, 'movies/index.html', context)

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('movies:index')
    else :
        review_form = ReviewForm()
    context = {
        'review_form':review_form,
    }
    return render(request, 'movies/create.html', context)