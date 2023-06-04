from django.shortcuts import render
from django.views import View
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages


# Create your views here.
# email validation
class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        user_email = data['email']
        if not validate_email(user_email):
            return JsonResponse({'email_error': 'email is not valid'}, status=400)
        if User.objects.filter(email=user_email).exists():
            return JsonResponse({'email_error': 'email already added'}, status=400)
        return JsonResponse({'email_valid': True})


# user name validation
class UserNameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username only should be alpha numeric'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'username already added'}, status=400)
        return JsonResponse({'username_valid': True})


class RegistrationViw(View):
    def get(self, request):
        return render(request, 'authentication/registration.html')

    def post(self, request):
        messages.error(request, 'succesfully ')
        return render(request, 'authentication/registration.html')
