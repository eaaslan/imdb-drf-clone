from watchlist_app.api.views import  (WatchListViewAV,WatchDetailViewAV,
                                      StreamPlatformAV,StreamPlatformDetailAV,
                                      ReviewList,ReviewDetail,ReviewCreate,StreamPlatformVS)
from django.urls import path,include

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')


urlpatterns = [
    path('list/', WatchListViewAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailViewAV.as_view(), name='movie-detail'),
    path('',include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name="streamplatform-detail"),
    path('<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),  
]
