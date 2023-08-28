from django.urls import path
from .views import (
    ClienteListView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView,
)

app_name = "customer"

urlpatterns = [
    path("list/", ClienteListView.as_view(), name="customer-list"),
    path("", ClienteCreateView.as_view(), name="customer-create"),
    path("<int:pk>/", ClienteUpdateView.as_view(), name="customer-update"),
    path("<int:pk>/delete/", ClienteDeleteView.as_view(), name="customer-delete"),
]

