from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from karaoke.models import Song, Voice, Playlist, UserScale
from .serializers import SongSerializer, VoiceSerializer, PlaylistSerializer, UserScaleSerializer

from django.db.models import Q

from .machine_learning.predict import predict
from config import settings


class MlAPIView(generics.ListCreateAPIView):
    """音声ファイルを機械学習に通すAPIクラス"""

    serializer_class = VoiceSerializer
    queryset = Voice.objects.all()

    def create(self, request):
        voiceSerializer = VoiceSerializer(data=request.data)
        voiceSerializer.is_valid(raise_exception=True)
        voiceSerializer.save()
        result = predict(settings.BASE_DIR + voiceSerializer.data["file"])
        artists = [i["artist"] for i in result]
        queryset = Song.objects.filter(
            Q(artist__name=artists[0])
            | Q(artist__name=artists[1])
            | Q(artist__name=artists[2])
            | Q(artist__name=artists[3])
            | Q(artist__name=artists[4])
        )
        songSerializer = SongSerializer(instance=queryset, many=True)
        response = [result, songSerializer.data]
        return Response(response, status=status.HTTP_201_CREATED)


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = (IsAuthenticated,)

class UserScaleViewSet(viewsets.ModelViewSet):
    """ユーザーの音域のCRUD用APIクラス"""

    queryset = UserScale.objects.all()
    serializer_class = UserScaleSerializer