from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.send_email_notification, name="index"),
    path('notify/', views.notify, name="notify")
]