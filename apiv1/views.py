from rest_framework import views, status, generics
from rest_framework.response import Response

from rest_framework.parsers import FileUploadParser

from karaoke.models import Song, Voice
from .serializers import SongSerializer, VoiceSerializer

from django.db.models import Q

from .machine_learning.predict import predict
import os
from config import settings


class MlAPIView(generics.ListCreateAPIView):
    """音声ファイルを機械学習に通すAPIクラス"""

    # parser_class = (FileUploadParser,)
    serializer_class = SongSerializer
    queryset = Song.objects.all()

    def create(self, request):
        voiceSerializer = VoiceSerializer(data=request.data)
        voiceSerializer.is_valid(raise_exception=True)
        voiceSerializer.save()
        print(predict(settings.BASE_DIR + voiceSerializer.data["file"]))
        result = predict(settings.BASE_DIR + voiceSerializer.data["file"])
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
