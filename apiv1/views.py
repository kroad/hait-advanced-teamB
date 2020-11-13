from rest_framework import status, generics
from rest_framework.response import Response

from karaoke.models import Song, Voice
from .serializers import SongSerializer, VoiceSerializer

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
        print(result)
        artists = list(result.keys())
        quesryset = Song.objects.filter(
            Q(artist__name=artists[0])
            | Q(artist__name=artists[1])
            | Q(artist__name=artists[2])
            | Q(artist__name=artists[3])
            | Q(artist__name=artists[4])
        )
        songSerializer = SongSerializer(instance=quesryset, many=True)

        return Response(songSerializer.data, status=status.HTTP_201_CREATED)
