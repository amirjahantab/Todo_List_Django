from django.urls import path
from . import views

urlpatterns = [
    path("", views.lists, name="lists"),
    path("<int:id>/", views.list_detail, name="detail"),
    path("delete/<int:id>", views.delete_list, name="delete_list")
]
