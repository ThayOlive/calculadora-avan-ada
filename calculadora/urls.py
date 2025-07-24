from django.contrib import admin
from django.urls import path, include
from calc_app import urls
import calc_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(calc_app.urls)),
]
