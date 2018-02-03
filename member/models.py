from django.db import models
# from django.contrib.auth.models import User
from club.models import Club
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    club = models.ManyToManyField(
            Club,
            related_name='club_member',
        )
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
        )
    # name = models.CharField(
    #         max_length=20,
    #         verbose_name='member name',
    #     )
    school = models.CharField(
            max_length=20,
            verbose_name='member school',
        )
    phone_number = models.CharField(
            max_length=20,
            verbose_name='phone number',
        )
    # email = models.CharField(
    #         max_length=50,
    #         verbose_name='member email',
    #     )
    # position = models.BooleanField(
    #         default=False,
    #     )


class Member(models.Model):
    pass


class Attendance(models.Model):
    member = models.ForeignKey(
            Member,
            on_delete=models.CASCADE,
            related_name='member_info',
        )
    attendance_check = models.BooleanField(
            default=False,
        )
    attendance_date = models.DateTimeField(
            auto_now_add=True,
            verbose_name='attendance date',
        )


class Absence(models.Model):
    attendance = models.OneToOneField(
            Attendance,
            on_delete=models.CASCADE,
        )
    minus = models.IntegerField(
            default=0,
        )
    minus_reason = models.CharField(
            max_length=100,
            verbose_name='minus reason',
        )
