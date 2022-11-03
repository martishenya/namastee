from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render, redirect
from django.views.generic import CreateView

from site_tamoj.models import Profile

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

# menu = ['О сайте', 'Обратная связь', 'Войти']

menu = [{'title': 'Главная', 'url_name': 'home' },
        {'title': 'О сайте', 'url_name': 'about' },
        {'title': 'Обратная связь', 'url_name': 'contact' },
        {'title': 'Войти', 'url_name': 'login' },
]
# Create your views here.

# def index(request):

def index(request):
    posts = Profile.objects.all()

    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница'
               }

    return render(request, 'site_tamoj/index.html', context=context)

def about(request):
    return render(request, 'site_tamoj/about.html', {'menu': menu, 'title': 'About'})

def contact(request):
    return HttpResponse('авторизация на сайте')

def categories(request, catid):
    if int(catid) > 5:
        print(type(catid))
        # return redirect('/', permanent=True)# если перманент то редирект устанавливается на постоянной основе
        return redirect('home', permanent=True) # чтобы избежать харкодинка установим имя url адреса(не явный url адрес)
    return HttpResponse(f'<h1>sdfgsdg</h1>{catid}')

# def login(request):
#     return HttpResponse('Авторизация')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Ошибка"))
            return redirect('login')
            pass
    else:
        return render(request, 'site_tamoj/login.html', { 'menu': menu,
        'title': 'Регистрация'})


def logout_user(request):
    logout(request)
    messages.success(request, ("Log out succes"))
    return redirect('home')


def register_user(request):


    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ('REgistration is suck'))
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'site_tamoj/register_user.html', {
        'form': form,
        'menu': menu,
        'title': 'Регистрация'
    })

