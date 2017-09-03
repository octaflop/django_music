from django.conf.urls import url, include
from web_endpoints.views import AlbumViewSet, SongViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
