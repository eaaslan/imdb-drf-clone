from watchlist_app.api.views import  MovieListView,MovieDetailView

from django.urls import path



urlpatterns = [
    path('list/', MovieListView.as_view(), name='movie-list'),
    path('<int:pk>', MovieDetailView.as_view(), name='movie-detail'),
]
