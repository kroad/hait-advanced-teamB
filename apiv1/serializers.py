from rest_framework import serializers

from karaoke.models import Song

class SongSerializer(serializers.ModelSerializer):
    
    artist_name = serializers.ReadOnlyField(source='artist.name')
    heighest_name = serializers.ReadOnlyField(source='heighest.name')
    lowest_name = serializers.ReadOnlyField(source='lowest.name')

    class Meta:
        model = Song
        fields = ['id','title','artist_name','heighest_name','lowest_name','artist','heighest','lowest']