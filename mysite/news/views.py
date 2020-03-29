from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail

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

def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'f': b})

def process(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid():
            # tieude = m.cleaned_data['title']
            # cc = m.cleaned_data['cc']
            # noidung = m.cleaned_data['content']
            # email = m.cleaned_data['email']
            # context = {'td': tieude, 'c': cc, 'b': noidung,'d': email }
            context2 = {'email_data': m}
            return render(request, 'news/print_email.html', context2)
        else:
            return HttpResponse("Form not validate")
    else:
        return HttpResponse("Khong phai post method")