from django.shortcuts import redirect, render
from .models import Review

def home(request):
  reviews = Review.objects.all()
  sort = request.GET.get("sort", "")

  if sort == "title": # 제목순
    reviews = reviews.order_by("title")
  elif sort == "grade": # 별점순
    reviews = reviews.order_by("-grade")
  elif sort == "time": # 러닝타임순
    reviews = reviews.order_by("-time")

  context = {
    "reviews": reviews
  }
  return render(request, template_name = "reviews/home.html", context=context)

def create(request):
  if request.method == "POST":
    title = request.POST["title"]
    year = request.POST["year"]
    genre = request.POST["genre"]
    grade = request.POST["grade"]
    time = request.POST["time"]
    review = request.POST["review"]
    director = request.POST["director"]
    actor = request.POST["actor"]

    Review.objects.create(
      title=title,
      year=year,
      genre=genre,
      grade=grade,
      time=time,
      review=review,
      director=director,
      actor=actor
    )
    return redirect("/")
  context = {
    'genre': Review.GENRE_CHOICE
  }
  return render(request, template_name = "reviews/create.html", context=context)

def detail(request, id):
  review = Review.objects.get(id=id)
  context = {
    "review": review, 
    "hour": review.time//60,
    "minute": review.time%60,
  }
  return render(request, template_name="reviews/detail.html", context=context)

def update(request, id):
  review = Review.objects.get(id=id)
  if request.method == "POST":
    title = request.POST["title"]
    year = request.POST["year"]
    genre = request.POST["genre"]
    grade = request.POST["grade"]
    time = request.POST["time"]
    review = request.POST["review"]
    director = request.POST["director"]
    actor = request.POST["actor"]

    Review.objects.filter(id=id).update(
      title=title,
      year=year,
      genre=genre,
      grade=grade,
      time=time,
      review=review,
      director=director,
      actor=actor
    )
    return redirect(f"/review/{id}")

  elif request.method == "GET":
    review = Review.objects.get(id=id)
    context = {
      "review": review
    }
    return render(request, template_name="reviews/update.html", context=context)

def delete(request, id):
  if request.method == "POST":
    Review.objects.filter(id=id).delete()
    return redirect('/')