from django.db import models

# Create your models here.


class Club(models.Model):
    club_name = models.CharField(
            max_length=50,
            verbose_name='club name',
        )
    club_image = models.ImageField()
    club_description = models.TextField(verbose_name='club description')

    def __str__(self):
        return self.club_name


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
