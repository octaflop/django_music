
# coding: utf-8

# # Intro to Web Development with Django
# # Faris Chebib

# ### A basic web page `web_page`

# Once django is set up, we can use a simple view to render a template.

# In[5]:


from django.shortcuts import render

def web_page(request):
    template_name = 'web_page/base.html'
    render(request, template_name, {})


# ### A basic web app `web_app`

# That was boring.
# 
# Let's do something more interesting...

# In[1]:


<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Album List</title>
  </head>
  <body>
    <h2>A basic album list</h2>
    {% for album in albums %}
    <h3>{{ album.title }} by {{album.artist }} ({{ album.year }})</h3>
    <h4>Songs:</h4>
      <ul>
      {% for song in album.songs %}
        <li>
          {{ song.track }} — {{ song.title }} {% if song.duration %}({{ song.duration }}){% endif %}
        </li>
      {% endfor %}
      </ul>
    {% endfor %}
  </body>
</html>


# In[ ]:


from django.shortcuts import render

from web_app.forms import SongForm


def basic_web_app(request):
    ctx = {}
    ctx['albums'] = [
        {
            'artist': 'Les Gordon',
            'title': 'Abyss',
            'year': '2016',
            'songs': [
                {
                    'track': 1,
                    'title': 'Abyss',
                    'duration': '3:13'
                },
                {
                    'track': 2,
                    'title': 'Shiho & Kyoko',
                    'duration': '2:58'
                },
            ]
        },
        {
            'artist': 'Same Gellaitry',
            'title': 'Escapism II',
            'year': '2016',
            'songs': [
                {
                    'track': 1,
                    'title': 'The Gateway',
                    'duration': '3:12'
                },
                {
                    'track': 2,
                    'title': 'Desert Mirage',
                    'duration': '5:00'
                },
                {
                    'track': 3,
                    'title': 'Jacket Weather',
                    'duration': None
                },
                {
                    'track': 4,
                    'title': 'Static Sleep',
                    'duration': ''
                }
            ]
        }
    ]
    template_name = 'web_app/basic.html'
    return render(request, template_name, ctx)


def dynamic_web_app(request):
    ctx = {}
    template_name = 'web_app/dynamic.html'
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            ctx['song'] = form.cleaned_data
    else:
        form = SongForm()
    ctx['form'] = form
    return render(request, template_name, ctx)


# ### A basic web db `web_db`

# Cool, but how do we store this data?

# In[ ]:


from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    artist = models.CharField(max_length=255)

    def __str__(self):
        return "{} by {} ({})".format(self.title, self.artist, self.year)


class Song(models.Model):
    title = models.CharField(max_length=255)
    track = models.PositiveIntegerField(blank=True)
    duration = models.CharField(max_length=15, blank=True)

    album = models.ForeignKey(Album)

    def __str__(self):
        return "{} ({})".format(self.title, self.track)


# In[ ]:


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


# In[ ]:


from django.conf.urls import url

from web_db import views

urlpatterns = [
    url(r'^albums/$', views.AlbumListView.as_view(), name='album-list'),
    url(r'^albums/(?P<pk>\d+)/$', views.AlbumDetailView.as_view(), name='album-detail'),
    url(r'^songs/$', views.SongListView.as_view(), name='song-list'),
    url(r'^songs/(?P<pk>\d+)/$', views.SongDetailView.as_view(), name='song-detail'),
]


# In[ ]:


from django.contrib import admin

from web_db import models


class SongAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class SongInline(admin.TabularInline):
    model = models.Song


class AlbumAdmin(admin.ModelAdmin):
    search_fields = ('title', 'artist', 'year',)
    inlines = (SongInline,)

admin.site.register(models.Album, AlbumAdmin)
admin.site.register(models.Song, SongAdmin)


# ### A basic web endpoint `web_endpoint`

# Now the front-end guy is yelling at us

# In[ ]:


from rest_framework import serializers

from web_db.models import Album, Song


class BasicSongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = ('title', 'track', 'duration',)


class AlbumSerializer(serializers.ModelSerializer):
    songs = BasicSongSerializer(many=True, source='song_set')

    class Meta:
        model = Album
        fields = ('title', 'artist', 'year', 'songs')

    def create(self, data):
        songs = data.pop('song_set')
        album = Album.objects.create(**data)
        for song in songs:
            Song.objects.create(album=album, **song)
        return album


class SongSerializer(serializers.ModelSerializer):
    album = AlbumSerializer()

    class Meta:
        model = Song
        fields = ('title', 'track', 'duration', 'album',)


# In[ ]:


from rest_framework import viewsets

from web_db.models import Album, Song

from web_endpoints.serializers import AlbumSerializer, SongSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


# In[ ]:


from django.conf.urls import url, include
from web_endpoints.views import AlbumViewSet, SongViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'songs', SongViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]


# ### BONUS!? `web_bonus`

# Python 3.6 + apistar = full on awesomness!

# In[ ]:


from apistar import Include, Route
from apistar.frameworks.asyncio import ASyncIOApp as App
from apistar.handlers import docs_urls, static_urls
from apistar.backends import django_orm
from apistar.backends.django_orm import Session
# from django.conf import settings  ## TODO: use the project settings

import os

REL = lambda * x: os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', *x))  # noqa

settings = {
    'DATABASES': {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': REL('db.sqlite3')
        }
    },
    'INSTALLED_APPS': ['web_bonus', 'web_db']
}


async def welcome(name=None):
    if name is None:
        return {'message': 'Welcome to API Star!'}
    return {'message': 'Welcome to API Star, %s!' % name}


async def create_album(
        session: Session, title: str, year: int, artist: str):
    album = session.Album(
        title=title,
        year=year,
        artist=artist)
    album.save()
    return {'id': album.id, 'title': album.title}


async def create_song(
        session: Session, title: str, album_id: int, track: int):
    album = session.Album.objects.get(id=album_id)
    song = session.Song(
        title=title,
        album=album,
        track=track)
    song.save()
    return {'id': song.id, 'title': song.title, 'track': track}


async def list_albums(session: Session):
    queryset = session.Album.objects.all()
    return [
        {'id': album.id, 'title': album.title, 'year': album.year}
        for album in queryset
    ]


async def list_songs(session: Session):
    queryset = session.Song.objects.all()
    return [
        {'id': song.id, 'title': song.title, 'track': song.track}
        for song in queryset
    ]


routes = [
    Route('/', 'GET', welcome),
    Route('/albums/', 'GET', list_albums),
    Route('/albums/', 'POST', create_album),
    Route('/songs/', 'GET', list_songs),
    Route('/songs/', 'POST', create_song),
    Include('/docs', docs_urls),
    Include('/static', static_urls)
]

app = App(
    routes=routes,
    settings=settings,
    commands=django_orm.commands,
    components=django_orm.components
    )


if __name__ == '__main__':
    app.main()

