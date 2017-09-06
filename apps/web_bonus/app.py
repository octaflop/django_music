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
