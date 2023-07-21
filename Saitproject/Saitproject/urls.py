from django.contrib import admin
from django.urls import path,include
from Sait.views import initialSite
from Sait.views import Honda
from Sait.views import Moskvich
from Sait.views import Nisann
from Sait.views import Toyta
from Sait.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',create_view),
    path('listview/',car_view),
    path('<int:id>/',car_detil_view),
    path('update/<int:id>/',update_view),
    path('delete/<int:id>',delete_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', include('Sait.urls')),
    path('initialSite.html',initialSite),
    path('Honda.html',Honda),
    path('Moskvich.html',Moskvich),
    path('Nisann.html',Nisann),
    path('Toyta.html',Toyta)
]
