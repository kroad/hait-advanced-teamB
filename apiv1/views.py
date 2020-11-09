from rest_framework import views, status
from rest_framework.response import Response
from playsound import playsound

from karaoke.models import Song
from .serializers import SongSerializer

from django.db.models import Q


class MLAPIView(views.APIView):
    """"音声ファイルを機械学習に通すAPIクラス"""

    def post(self, request, *args, **kwargs):
        file = self.request.data["voiceFile"]
        print(file)
        print(file.size)
        print(type(file))
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
