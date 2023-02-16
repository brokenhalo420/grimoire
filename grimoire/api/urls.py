from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users_list),
    path('anime/', views.get_anime_list),
    path('ranked/', views.get_top_hundred_anime),
    path('create_user/', views.create_user),
    path('anime_info/<str:title>', views.get_anime_details)
]