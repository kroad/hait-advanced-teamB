from django.db import models
from django.contrib.auth import get_user_model


class Voice(models.Model):
    """音声ファイル"""

    class Meta:
        db_table = "voice"

    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name


class Scale(models.Model):
    """音階"""

    class Meta:
        db_table = "scale"

    japan = models.CharField(verbose_name="音階名(日本式)", max_length=10)
    universal = models.CharField(verbose_name="音階名(国際表記)", max_length=10)

    def __str__(self):
        return self.japan


class Artist(models.Model):
    """歌手"""

    class Meta:
        db_table = "artist"

    name = models.CharField(verbose_name="歌手", max_length=25)

    def __str__(self):
        return self.name


class Song(models.Model):
    """曲モデル"""

    class Meta:
        db_table = "song"

    title = models.CharField(verbose_name="タイトル", max_length=50)
    z_highest = models.ForeignKey(
        Scale,
        verbose_name="地声最高音",
        on_delete=models.PROTECT,
        related_name="z_highest",
        null=True,
        blank=True,
    )
    z_lowest = models.ForeignKey(
        Scale,
        verbose_name="地声最低音",
        on_delete=models.PROTECT,
        related_name="z_lowest",
        null=True,
        blank=True,
    )
    u_highest = models.ForeignKey(
        Scale,
        verbose_name="裏声最高音",
        on_delete=models.PROTECT,
        related_name="u_highest",
        null=True,
        blank=True,
    )
    u_lowest = models.ForeignKey(
        Scale,
        verbose_name="裏声最低音",
        on_delete=models.PROTECT,
        related_name="u_lowest",
        null=True,
        blank=True,
    )
    artist = models.ForeignKey(
        Artist,
        verbose_name="歌手",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.title

class Playlist(models.Model):
    """プレイリスト"""

    class Meta:
        db_table = "playlist"

    name = models.CharField(verbose_name="プレイリスト名", max_length=25)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name = 'ユーザー',
    )
    songs = models.ManyToManyField(Song, verbose_name='曲')
    def __str__(self):
        return self.name
class UserScale(models.Model):
    """ユーザーの最高音・最低音"""

    class Meta:
        db_table = "user_scale"

    user = models.OneToOneField(get_user_model(), verbose_name="ユーザー", on_delete=models.CASCADE)
    z_highest = models.ForeignKey(
        Scale,
        verbose_name="地声最高音",
        on_delete=models.PROTECT,
        related_name="user_z_highest",
        null=True,
        blank=True,
    )
    z_lowest = models.ForeignKey(
        Scale,
        verbose_name="地声最低音",
        on_delete=models.PROTECT,
        related_name="user_z_lowest",
        null=True,
        blank=True,
    )
    u_highest = models.ForeignKey(
        Scale,
        verbose_name="裏声最高音",
        on_delete=models.PROTECT,
        related_name="user_u_highest",
        null=True,
        blank=True,
    )
    u_lowest = models.ForeignKey(
        Scale,
        verbose_name="裏声最低音",
        on_delete=models.PROTECT,
        related_name="user_u_lowest",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.user.username