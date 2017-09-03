from django.conf.urls import url

from web_db import views

urlpatterns = [
    url(r'^albums/$', views.AlbumListView.as_view(), name='album-list'),
    url(r'^albums/(?P<pk>\d+)/$', views.AlbumDetailView.as_view(), name='album-detail'),
    url(r'^songs/$', views.SongListView.as_view(), name='song-list'),
    url(r'^songs/(?P<pk>\d+)/$', views.SongDetailView.as_view(), name='song-detail'),
]
