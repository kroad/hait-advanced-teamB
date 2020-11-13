from rest_framework import views, status, generics
from rest_framework.response import Response

from rest_framework.parsers import FileUploadParser

from karaoke.models import Song, Voice
from .serializers import SongSerializer, VoiceSerializer

from django.db.models import Q

from .machine_learning.predict import predict
import os
from config import settings


class TestAPIView(generics.ListCreateAPIView):
    """test用"""

    # parser_class = (FileUploadParser,)
    serializer_class = VoiceSerializer
    queryset = Voice.objects.all()

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


class MLAPIView(views.APIView):
    """"音声ファイルを機械学習に通すAPIクラス"""

    def get(self, *args, **kwargs):
        serializer = SongSerializer(instance=Song.objects.all(), many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        file = self.request.data["voiceFile"]
        print(request)
        print(request.data)
        print(request.FILES)
        print(file)
        print(file)
        # model = pd.read_pickle()
        # result = model.predict(file)
        artists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        quesryset = Song.objects.filter(
            Q(artist=artists[0])
            | Q(artist=artists[1])
            | Q(artist=artists[2])
            | Q(artist=artists[3])
            | Q(artist=artists[4])
            | Q(artist=artists[5])
            | Q(artist=artists[6])
            | Q(artist=artists[7])
            | Q(artist=artists[8])
            | Q(artist=artists[9])
        )
        serializer = SongSerializer(instance=quesryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
