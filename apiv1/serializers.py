from rest_framework import serializers

from karaoke.models import Song


class SongSerializer(serializers.ModelSerializer):

    artist_name = serializers.ReadOnlyField(source="artist.name")
    z_heighest_japan = serializers.ReadOnlyField(source="z_heighest.japan")
    z_heighest_universal = serializers.ReadOnlyField(source="z_heighest.universal")
    u_heighest_japan = serializers.ReadOnlyField(source="u_heighest.japan")
    u_heighest_universal = serializers.ReadOnlyField(source="u_heighest.universal")
    z_lowest_japan = serializers.ReadOnlyField(source="z_lowest.japan")
    z_lowest_universal = serializers.ReadOnlyField(source="z_lowest.universal")
    u_lowest_japan = serializers.ReadOnlyField(source="u_lowest.japan")
    u_lowest_universal = serializers.ReadOnlyField(source="u_lowest.universal")

    class Meta:
        model = Song
        fields = [
            "id",
            "title",
            "artist_name",
            "z_heighest_japan",
            "z_heighest_universal",
            "u_heighest_japan",
            "u_heighest_universal",
            "z_lowest_japan",
            "z_lowest_universal",
            "u_lowest_japan",
            "u_lowest_universal",
            "artist",
        ]
