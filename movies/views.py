from django.shortcuts import redirect, render
from .forms import ReviewForm
from .models import Review


def index(request):
    reviews = Review.objects.all()
    movie_img = {
        '탑건':"{% static 'movies/탑건.jpg' %}",
    }
    context = {
        "reviews": reviews,
        '탑건':"{% static 'movies/탑건.jpg' %}",
        
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
    return render(request, "movies/create.html", context)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()

    return redirect("movies:index")


def search(request):
    all_movie = Review.objects.all()
    search_movie = request.GET.get("search", "")
    if search_movie:
        return_movie = all_movie.filter(title__icontains=search_movie)

        context = {
            "search_movie": return_movie,
        }

    return render(request, "movies/index.html", context)

def genres(request, pk):

    genres_table = {
        1: "액션",
        2: "스릴러",
        3: "코미디",
        4: "로맨스",
        5: "SF",
        6: "드라마",
        7: "애니메이션",
    }
    result_genre = genres_table.get(pk)
    all_genre = Review.objects.filter(genre=result_genre)

    context = {
        "all_genre": all_genre,
    }

    return render(request, "movies/index.html", context)