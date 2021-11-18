from django.urls import path
from .controllers.main import MainController
from .controllers.profile import ProfileController

urlpatterns = [
    path('main/', MainController, name = 'Main'),
    path('profile/', ProfileController, name = 'Profile')
]
