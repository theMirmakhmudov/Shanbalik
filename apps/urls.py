from django.urls import path
from apps.views import main
urlpatterns = [
    path('', main, name='main')
]

