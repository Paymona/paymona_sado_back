from django.urls import path
from .controllers.login import LoginController
from .controllers.register import RegisterController

urlpatterns = [
    path('login/', LoginController, name='Login'),
    path('register/', RegisterController, name='Register')
]