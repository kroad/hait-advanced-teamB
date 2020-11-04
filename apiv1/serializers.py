from rest_framework import serializers

from karaoke.models import Song


class SongSerializer(serializers.ModelSerializer):

    artist_name = serializers.ReadOnlyField(source="artist.name")

    z_heighest_japan = serializers.ReadOnlyField(source="z_heighest.japan")
    z_heighest_universal = serializers.ReadOnlyField(source="z_heighest.universal")
    z_heighest_id = serializers.ReadOnlyField(source="z_heighest.id")

    u_heighest_japan = serializers.ReadOnlyField(source="u_heighest.japan")
    u_heighest_universal = serializers.ReadOnlyField(source="u_heighest.universal")
    u_heighest_id = serializers.ReadOnlyField(source="u_heighest.id")

    z_lowest_japan = serializers.ReadOnlyField(source="z_lowest.japan")
    z_lowest_universal = serializers.ReadOnlyField(source="z_lowest.universal")
    z_lowest_id = serializers.ReadOnlyField(source="z_lowest.id")

    u_lowest_japan = serializers.ReadOnlyField(source="u_lowest.japan")
    u_lowest_universal = serializers.ReadOnlyField(source="u_lowest.universal")
    u_lowest_id = serializers.ReadOnlyField(source="u_lowest.id")

    class Meta:
        model = Song
        fields = [
            "id",
            "title",
            "artist_name",
            "z_heighest_japan",
            "z_heighest_universal",
            "z_heighest_id",
            "u_heighest_japan",
            "u_heighest_universal",
            "u_heighest_id",
            "z_lowest_japan",
            "z_lowest_universal",
            "z_lowest_id",
            "u_lowest_japan",
            "u_lowest_universal",
            "u_lowest_id",
            "artist",
        ]
