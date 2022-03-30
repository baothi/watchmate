from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
# from watchlist_app.api.views import MoveListAv, MovieDetailAV, StreamPlatformAv
from watchlist_app.api.views import WatchListAv, WatchDetailAV , StreamPlatformAv


urlpatterns = [
    path('list/', WatchListAv.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),

    path('stream/', StreamPlatformAv.as_view(), name='movie-list'),
]