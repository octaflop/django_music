from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from web_db.models import Album, Song


class AlbumDetailView(DetailView):
    model = Album
    context_object_name = 'album'


class AlbumListView(ListView):
    model = Album
    context_object_name = 'albums'


class SongDetailView(DetailView):
    model = Song
    context_object_name = 'song'


class SongListView(ListView):
    model = Song
    context_object_name = 'songs'
