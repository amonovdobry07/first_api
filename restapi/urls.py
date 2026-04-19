from django.urls import path
from .views import CarsApiView, CartDetailView, CreateCarView, CarUptadeDeleteView, DirectPasswordResetView

urlpatterns = [
    path("cars/", CarsApiView.as_view(), name = "cars-list" ), 
    path("cars/<int:id>/", CartDetailView.as_view(), name = "car-detail"), 
    path("cars/create/", CreateCarView.as_view(), name = "car-create"),
    path("cars/<int:id>/uptade-delete/", CarUptadeDeleteView.as_view(), name = "car-uptade-detele"),
    path('auth/password/reset-direct/', DirectPasswordResetView.as_view(), name='password_reset_direct'),   
]






