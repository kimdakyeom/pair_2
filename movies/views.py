from django.shortcuts import redirect, render
from .forms import ReviewForm
from .models import Review


def index(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, "movies/index.html", context)


def create(request):
    
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("movies:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "movies/create.html", context)


def main(request):

    return render(request, "movies/main.html")


def detail(request, pk):
    review_get = Review.objects.get(pk=pk)

    context = {"review_get": review_get}

    return render(request, "movies/detail.html", context)


def update(request, pk):
    update_movie = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=update_movie)
        if review_form.is_valid():
            review_form.save()
            return redirect("movies:detail", pk)
    else:
        review_form = ReviewForm(instance=update_movie)
    context = {
        "review_form": review_form,
        "update_movie": update_movie,
    }
    return render(request, "movies:create.html", context)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()

    return redirect("movies:index")


def search(request):
    all_movie = Review.objects.all()
    search_movie = request.GET.get("search","")
    if search_movie:
        all_movie.filter( title__icontains = search_movie )

        context={
            'search_movie': search_movie,
        }

    return render(request ,'movies:index',context)

