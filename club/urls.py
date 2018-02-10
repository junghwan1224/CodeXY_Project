from django.urls import path
from . import views

app_name = 'club'

urlpatterns = [
    path('entry/', views.entry_club, name='entry_club'),
    path('admin_club/<int:pk>/', views.admin_club, name='admin_club'),
    path('as_member_club/<int:pk>/', views.as_member_club, name='as_member_club'),
]
