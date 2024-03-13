from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="MartHome"),
    path("about/", views.about, name="AboutUS"),
    path("contact/", views.contact, name="contactUS"),
    path("tracker/", views.tracker, name="track"),
    path("search/", views.search, name="search"),
    path("products/<int:myid>", views.products, name="products"),
    path("checkout/", views.checkout, name="checkout")
]
