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
