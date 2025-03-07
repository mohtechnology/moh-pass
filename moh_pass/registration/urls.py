from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name="register"),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('approved/', views.approved_users, name='approved'),
    path('pass_detail/<str:unique_id>/', views.pass_detail, name='pass_detail'),
    path('validate/<str:unique_id>/', views.validate, name='validate'),
]
