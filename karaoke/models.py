from django.db import models

class Scale(models.Model):
    """音階"""

    class Meta:
        db_table = 'scale'

    name = models.CharField(verbose_name='音階名',max_length=10)

    def __str__(self):
        return self.name
    

class Artist(models.Model):
    """歌手"""

    class Meta:
        db_table = 'artist'

    name = models.CharField(verbose_name='歌手',max_length=25)

    def __str__(self):
        return self.name



class Song(models.Model):
    """曲モデル"""

    class Meta:
        db_table = 'song'

    title = models.CharField(verbose_name='タイトル',max_length=50)
    heighest = models.ForeignKey(Scale, verbose_name='最高音', on_delete=models.PROTECT, related_name='heighest_scale')
    lowest = models.ForeignKey(Scale, verbose_name='最低音', on_delete=models.PROTECT, related_name='lowest_scale')
    artist = models.ForeignKey(Artist, verbose_name='歌手', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.title