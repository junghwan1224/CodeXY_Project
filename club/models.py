from django.db import models
from django.conf import settings
# Create your models here.


class Club(models.Model):
    club_name = models.CharField(
            max_length=50,
            verbose_name='club name',
        )
    club_image = models.ImageField(
            upload_to='club/%Y/%m/%d/',
            blank=True,
            null=True,
        )
    club_description = models.TextField(
            verbose_name='club description',
            blank=True,
            null=True,
        )
    position = models.BooleanField(
            default=False,
        )
    # positon 0=admin, 1=member, 2=not member

    def __str__(self):
        return self.club_name


class ApplyList(models.Model):
    club = models.ForeignKey(
            Club,
            on_delete=models.CASCADE,
            related_name='applylist_club',
        )
    user = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='applylist_user',
        )


class ClubRule(models.Model):
    main_theme = models.CharField(
            max_length=30,
            verbose_name='main theme',
        )
    sub_theme = models.CharField(
            max_length=30,
            verbose_name='sub theme',
        )
    rule = models.TextField(verbose_name='rule')
    club = models.ForeignKey(
            Club,
            on_delete=models.CASCADE,
            related_name='club',
        )
