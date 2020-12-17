from django.db.models import fields
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from karaoke.models import Song, Voice, Playlist, Scale, Artist

from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model
from djoser.conf import settings


class VoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voice
        fields = "__all__"


# class ScaleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Scale
#         fields = "__all__"


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):

    # artist_name = serializers.ReadOnlyField(source="artist.name")
    artist = ArtistSerializer()

    z_highest_japan = serializers.ReadOnlyField(source="z_highest.japan")
    z_highest_universal = serializers.ReadOnlyField(source="z_highest.universal")
    z_highest_id = serializers.ReadOnlyField(source="z_highest.id")

    u_highest_japan = serializers.ReadOnlyField(source="u_highest.japan")
    u_highest_universal = serializers.ReadOnlyField(source="u_highest.universal")
    u_highest_id = serializers.ReadOnlyField(source="u_highest.id")

    z_lowest_japan = serializers.ReadOnlyField(source="z_lowest.japan")
    z_lowest_universal = serializers.ReadOnlyField(source="z_lowest.universal")
    z_lowest_id = serializers.ReadOnlyField(source="z_lowest.id")

    u_lowest_japan = serializers.ReadOnlyField(source="u_lowest.japan")
    u_lowest_universal = serializers.ReadOnlyField(source="u_lowest.universal")
    u_lowest_id = serializers.ReadOnlyField(source="u_lowest.id")

    # z_highest = ScaleSerializer()
    # z_lowest = ScaleSerializer()
    # u_highest = ScaleSerializer()
    # u_lowest = ScaleSerializer()

    class Meta:
        model = Song
        fields = [
            "id",
            "title",
            "artist",
            "z_highest_japan",
            "z_highest_universal",
            "z_highest_id",
            "u_highest_japan",
            "u_highest_universal",
            "u_highest_id",
            "z_lowest_japan",
            "z_lowest_universal",
            "z_lowest_id",
            "u_lowest_japan",
            "u_lowest_universal",
            "u_lowest_id",
        ]
        # fields = [
        #     "id",
        #     "title",
        #     "artist",
        #     "z_highest",
        #     "z_lowest",
        #     "u_highest",
        #     "u_lowest",
        # ]


class PlaylistSerializer(WritableNestedModelSerializer):
    songs = SongSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ["id", "name", "user", "songs"]


User = get_user_model()


class SpecialUserSerializer(UserSerializer):
    playlist_set = PlaylistSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "username", "playlist_set"]
        read_only_fields = (settings.LOGIN_FIELD,)
