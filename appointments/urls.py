from django.urls import path
from . import views

urlpatterns=[
    path('book/',views.book_appointment,name='book_appointment'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),


]