from django.shortcuts import render

from django.http import HttpResponse


def index(request, name="World"):
    greeting = f"Hello {name}, welcome to the Django app!"
    return render(request, "hello/index.html", {'greeting': greeting})