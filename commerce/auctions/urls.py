from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.create, name="create"),
    path("item/<int:id>", views.item, name="item"),
    path("categories", views.category, name="category"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("myitems",views.myitems, name = "myitems")
]
