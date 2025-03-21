from django.contrib import admin
from django.urls import path
from . import views  # Import views from the same folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("predict/", views.predict, name='predict'),
    path('predict/result',views.result, name='result')# Make sure 'home' is defined in views.py
]

