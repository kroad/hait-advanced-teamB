from rest_framework import serializers

from karaoke.models import Song


class SongSerializer(serializers.ModelSerializer):

    artist_name = serializers.ReadOnlyField(source="artist.name")
    heighest_japan = serializers.ReadOnlyField(source="heighest.japan")
    heighest_universal = serializers.ReadOnlyField(source="heighest.universal")
    lowest_japan = serializers.ReadOnlyField(source="lowest.japan")
    lowest_universal = serializers.ReadOnlyField(source="lowest.universal")

    class Meta:
        model = Song
        fields = [
            "id",
            "title",
            "artist_name",
            "heighest_japan",
            "heighest_universal",
            "lowest_japan",
            "lowest_universal",
            "artist",
            "heighest",
            "lowest",
        ]
