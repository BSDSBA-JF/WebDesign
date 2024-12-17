from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("brian", views.brian, name = "brian"),
    path("jf", views.jf, name = "jf"),
    path("<str:name>", views.greet, name = "greet")
]