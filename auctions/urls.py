from django.urls import path

from . import views

urlpatterns = [
   
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("list/<str:id>", views.show_list, name='show_list'),
    path("categories", views.show_categories, name='show_categories'),
    path("create_list", views.create_list, name='create_list'),
    path("bid/<str:id>", views.create_bid, name='create_bid'),
    path("comment/<str:id>", views.create_comment, name='create_comment'),
    path("categories/<str:id>", views.show_category, name='show_category'),
    path("watchlist/<str:id>", views.show_watchlist, name='show_watchlist'),
    path("edit/<str:id>", views.edit_list, name='edit_list'),
    path("add_watch/<str:id>", views.add_watchlist, name='add_watchlist'),

]
