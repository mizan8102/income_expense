from .views import RegistrationViw, UserNameValidationView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('register', RegistrationViw.as_view(), name='register'),
    path('username-validation', csrf_exempt(UserNameValidationView.as_view()), name='user-name-validation')
]
