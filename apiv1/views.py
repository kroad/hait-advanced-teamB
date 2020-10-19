from rest_framework import generics, viewsets

from karaoke.models import Song
from .serializers import SongSerializer

from django_filters import rest_framework as filters

from django.db.models import Q

# ModelViewSetとdjango-filterを使ったやつ
class SongFilter(filters.FilterSet):
    """曲モデル用フィルタクラス"""
    heighest__lte = filters.NumberFilter(field_name='heighest', lookup_expr='lte')
    lowest__gte = filters.NumberFilter(field_name='lowest', lookup_expr='gte')

    class Meta:
        model = Song
        fields = '__all__'

class SongViewSet(viewsets.ModelViewSet):
    """曲モデルのCRUD用APIクラス"""

    queryset = Song.objects.all()
    serializer_class = SongSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = SongFilter

# 汎用クラスViewを使ったやつ
class SongListAPIView(generics.ListAPIView):
    """曲モデルの取得APIクラス"""

    serializer_class = SongSerializer
    
    def get_queryset(self):
        queryset = Song.objects.all()
        if self.request.query_params :
            artist1 = self.request.GET.get('artist1')
            artist2 = self.request.GET.get('artist2')
            heighest = self.request.GET.get('heighest')
            lowest = self.request.GET.get('lowest')
            # model = pd.read_pickle()
            # result = model.predict()
            return Song.objects.filter(Q(artist=artist1)|Q(artist=artist2),heighest__lte=heighest,lowest__gte=lowest)
        return queryset