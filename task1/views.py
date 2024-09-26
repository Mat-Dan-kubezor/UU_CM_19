from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .models import *


def check_form(info, username, password, repeat_password, age):
    if password != repeat_password:
        info["error"] = "Пароли не совпадают"
    elif int(age) < 18:
        info["error"] = "Вы должны быть старше 18"
    elif Buyer.objects.filter(name=username).exists():
        info["error"] = "Пользователь уже существует"


def sign_up_by_html(request):
    info = dict()
    if request.method == 'POST':
        # Получаем данные из формы
        username = request.POST.get("username")
        password = request.POST.get("password")
        repeat_password = request.POST.get("repeat_password")
        age = request.POST.get("age")

        # Проверяем данные формы
        check_form(info, username, password, repeat_password, age)
        if "error" not in info:
            Buyer.objects.create(name=username, balance=0.00, age=age)
            return HttpResponse(f"<p align=center>Приветствуем, {username}!</p>")

    return render(request, 'registration_page.html', context=info)


def platform(request):
    return render(request, 'platform.html')


def games(request):
    # context = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay2"]}
    games = Game.objects.all()
    context = {
        'games': games,
    }
    return render(request, 'games.html', context)


def cart(request):
    return render(request, 'cart.html')
