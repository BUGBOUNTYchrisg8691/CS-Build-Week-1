from django.shortcuts import render


# Create your views here.
def index(req, *args, **kwargs):
    return render(req, "client/index.html")
