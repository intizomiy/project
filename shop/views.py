from django.shortcuts import render
from .models import Index


def index(request):
    i = Index.objects.all()
    context = {
        'index':i
    }
    return render(request, "home_index.html", context)


