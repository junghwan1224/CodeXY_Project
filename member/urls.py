from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('member_info/', views.member_info, name='member_info'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]
