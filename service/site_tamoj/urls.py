from django.urls import path, include

from . import views
from .views import *

urlpatterns = [
    # path('', views.signup, name='signup'),
    path('', index, name= 'home'), #установили имя для удобства дальнейшего объявления
    path('about/', about, name= 'about'),
    path('contact/', contact, name= 'contact'),
    path('login/', login_user, name= 'login'),
    path('logout/', logout_user, name= 'logout'),
    path('register_user/', register_user, name= 'register_user'),
    path('dataset/', dataset, name= 'dataset'),
    # path('categories/<int:catid>/', categories),

    # path('account/', include('django.contrib.auth.urls')),
    # path('', views.index, name='index'),
]

