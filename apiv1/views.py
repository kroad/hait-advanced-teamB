from rest_framework import generics

from karaoke.models import Song, Scale
from .serializers import SongSerializer

from django.db.models import Q

# 汎用クラスViewを使ったやつ
class SongListAPIView(generics.ListAPIView):
    """曲モデルの取得APIクラス"""

    serializer_class = SongSerializer

    def get_queryset(self):
        queryset = Song.objects.all()
        if self.request.query_params:
            z_lowest = self.request.GET.get("z_lowest")
            z_heighest = self.request.GET.get("z_heighest")
            # 後で戻す
            # u_heighest = self.request.GET.get("u_heighest")
            # model = pd.read_pickle()
            # result = model.predict()
            artists = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            return Song.objects.filter(
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
            ).filter(
                z_heighest__lte=Scale.objects.get(japan=z_heighest).id,
                z_lowest__gte=Scale.objects.get(japan=z_lowest).id,
            )
        return queryset