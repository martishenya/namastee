from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render, redirect
from django.views.generic import CreateView
import pandas as pd
from site_tamoj.models import Profile
import psycopg2
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from .forms import UserCreationForm, SignUpForm

# menu = ['О сайте', 'Обратная связь', 'Войти']

menu = [{'title': 'Главная', 'url_name': 'home' },
        {'title': 'О сайте', 'url_name': 'about' },
        {'title': 'Обратная связь', 'url_name': 'contact' },
        {'title': 'Войти', 'url_name': 'login' },
]
# Create your views here.

# def index(request):

def index(request):
    posts = Profile.objects.filter(name = 'какое')
    print(posts)
    con = psycopg2.connect(
        # dbname="my_table_name",
        database="hackdb",
        user="postgres",
        password="12345",
        host="127.0.0.1",
        port="5432"
    )

    print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT topic from my_table_name")
    dct = []
    rows = cur.fetchall()
    for row in rows:
        dct.append(row)


    print("Operation done successfully")
    con.close()

    context = {'dct': dct,
               'menu': menu,
               'title': 'Главная страница'
               }

    return render(request, 'site_tamoj/index.html', context=context)


posts = Profile.objects.all()
print(list(posts))


def about(request):

    return render(request, 'site_tamoj/about.html', {'title': 'About'})

def contact(request):
    return HttpResponse('авторизация на сайте')

def properties(request, region):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('properties')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("Ошибка"))
            return redirect('login')
            pass
    else:
        return render(request, 'site_tamoj/login.html', { 'menu': menu,
        'title': 'Регистрация'})



# def vivod(request, region):
#     if request.method == "POST":
#         return render(request, 'site_tamoj/vivod.html', {'region': region})
#     else:
#         return redirect('vivo')


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
            return redirect('properties')
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
    return redirect('login')


# def register_user(request):
#
#
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username = username, password = password)
#             login(request, user)
#             messages.success(request, ('REgistration is suck'))
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'site_tamoj/register_user.html', {
#         'form': form,
#         'menu': menu,
#         'title': 'Регистрация'
#     })


def register_user(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, ('REgistration is suck'))
            return redirect('properties')
        else:
            messages.success(request, ("Что-то не так с формой"))
    else:
        form = SignUpForm()

    return render(request, 'site_tamoj/register_user.html', {
        'form': form,
        'menu': menu,
        'title': 'Регистрация'
    })
def dataset(request):

    df=pd.read_csv("dataset_per_country (1).csv")
    df = pd.DataFrame(data=df)

    mydict = {
        "df": df.to_html()
    }
    return render(request, 'site_tamoj/dataset.html', context=mydict)


#
# df = pd.read_csv('full_dataset_top_15.csv')
#
#
# df.columns = [c.lower() for c in df.columns] # PostgreSQL doesn't like capitals or spaces
#
# from sqlalchemy import create_engine
#
# engine = create_engine('postgresql://postgres:12345@localhost:5432/hackdb')
#
# df.to_sql("my_table_name", engine,if_exists='append')


# import psycopg2
#
# con = psycopg2.connect(
#     # dbname="my_table_name",
#     database="hackdb",
#     user="postgres",
#     password="12345",
#     host="127.0.0.1",
#     port="5432"
# )
#
# print("Database opened successfully")
# cur = con.cursor()
# cur.execute("SELECT topic from my_table_name")
#
# rows = cur.fetchall()
# for row in rows:
#     print("topic =", row[0], "\n")
#
# print("Operation done successfully")
# con.close()
