from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('about/', views.about, name='about'),
    path('result/', views.result, name='result'),  # ✅ Ensure correct path
]
