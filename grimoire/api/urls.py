from django.urls import path
from . import views

urlpatterns = [
    path('anime/', views.get_anime_list),
    path('ranked/<int:number>/', views.get_top_hundred_anime),
    path('anime_info/<str:title>/', views.get_anime_details),
    path('favorite/<int:anime_id>/<str:username>', views.add_anime_to_favorites),
    path('watch_later/<int:anime_id>/<str:username>', views.add_anime_to_watch_later),
    path('watched/<int:anime_id>/<str:username>', views.add_anime_to_watched),
    path('favorites/<str:username>', views.get_favorites),
    path('watch_later/<str:username>', views.get_watch_later),
    path('watched/<str:username>', views.get_watched),
    path('favorites/remove/<int:anime_id>/<str:username>', views.remove_anime_from_favorites),
    path('watch_later/remove/<int:anime_id>/<str:username>', views.remove_anime_from_watch_later),
    path('watched/remove/<int:anime_id>/<str:username>', views.remove_anime_from_watched),
]