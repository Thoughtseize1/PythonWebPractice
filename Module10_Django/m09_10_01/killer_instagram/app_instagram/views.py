from django.shortcuts import render

# Create your views here.


def main(request):
    cat_desc = "Шелдон, глупый рыжий кошак, который постоянно подводит всех вокруг себя своей удивительной неспособностью думать. Его маленький мозг, как будто сделан из ваты. Тем не менее, вся его глупость и неловкость не могут помешать ему быть милым и обаятельным кошачьим существом. Возможно, именно благодаря своей глупости Шелдон становится источником смеха и радости для всех вокруг него."
    return render(
        request,
        "app_instagram\index.html",
        context={"title": "Sheldon's site", "cat_description": cat_desc},
    )


def upload(request):
    return render(
        request,
        "app_instagram/upload.html",
        context={"title": "Upload picture"}
    )


def pictures(request):
    return render(
        request,
        "app_instagram/pictures.html",
        context={"title": "Pictures"}
    )