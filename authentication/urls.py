from .views import RegistrationViw
from django.urls import path

urlpatterns = [
    path('register', RegistrationViw.as_view(), name='register')
]
