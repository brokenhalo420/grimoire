from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ranking/<int:number>/', views.get_ranking, name='ranking'),
    path('favorite/<int:anime_id>', views.add_to_favorite, name="add_to_favorite"),
    path('watch_later/<int:anime_id>', views.add_to_watch_later, name="add_to_watch_later"),
    path('watched/<int:anime_id>', views.add_to_watched, name="add_to_watched"),
    path('favorites',views.get_favorites,name='favorites'),
    path('watch_later', views.get_watch_later, name='watch_later'),
    path('watched', views.get_watched, name='watched'),
    path('favorites/remove/<int:anime_id>',views.remove_from_favorites, name="remove_from_favorites"),
    path('watch_later/remove/<int:anime_id>',views.remove_from_watch_later, name="remove_from_watch_later"),
    path('watched/remove/<int:anime_id>',views.remove_from_watched, name="remove_from_watched"),
]