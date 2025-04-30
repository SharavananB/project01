from django.urls import path

from app import views

urlpatterns = [
    path('',views.index),
    path('why',views.why),
    path('trainer',views.trainer),
    path('contact',views.contact),
]