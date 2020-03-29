from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm

# Create your views here.
def index(request):
    return HttpResponse("xin chao")
def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f': a})
def save_news(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Luu oke")
        else:
            return HttpResponse("Ko dc validate")
    else:
        return HttpResponse("khong phai post request")