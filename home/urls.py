from django.urls import path

from home.controllers.assess import Assess
from .controllers.main import MainController
from .controllers.profile import ProfileController
from .controllers.record import Record

urlpatterns = [
    path('main/', MainController, name = 'Main'),
    path('profile/', ProfileController, name = 'Profile'),
    path('record/', Record, name = 'Запись'),
    path('assess/', Assess, name='Оценить')
]
