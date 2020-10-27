from rest_framework import generics, viewsets

from karaoke.models import Song
from .serializers import SongSerializer

from django.db.models import Q

# 汎用クラスViewを使ったやつ
class SongListAPIView(generics.ListAPIView):
    """曲モデルの取得APIクラス"""

    serializer_class = SongSerializer

    def get_queryset(self):
        queryset = Song.objects.all()
        if self.request.query_params:
            artist1 = self.request.GET.get("artist1")
            artist2 = self.request.GET.get("artist2")
            artist3 = self.request.GET.get("artist3")
            artist4 = self.request.GET.get("artist4")
            artist5 = self.request.GET.get("artist5")
            artist6 = self.request.GET.get("artist6")
            artist7 = self.request.GET.get("artist7")
            heighest = self.request.GET.get("heighest")
            lowest = self.request.GET.get("lowest")
            # model = pd.read_pickle()
            # result = model.predict()
            return Song.objects.filter(
                Q(artist=artist1)
                | Q(artist=artist2)
                | Q(artist=artist3)
                | Q(artist=artist4)
                | Q(artist=artist5)
                | Q(artist=artist6)
                | Q(artist=artist7),
                heighest__lte=heighest,
                lowest__gte=lowest,
            )
        return queryset