from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("", views.home, name="home"),
    path("get_data/", views.get_data, name="get_data"),
    path("add_user/", views.add_user, name="add_user"),
    path("print_users/", views.print_users, name="print_users"),
]
