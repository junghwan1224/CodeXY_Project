from django.urls import path
from . import views

app_name = 'club'

urlpatterns = [
    path('entry/', views.entry_club, name='entry_club'),
]
