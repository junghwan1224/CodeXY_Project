from django.db import models
from django.contrib.auth.models import User
from club.models import Club
# Create your models here.


class Profile(models.Model):
    club = models.ForeignKey(
            Club,
            on_delete=models.CASCADE,
            related_name='club_member',
        )
    user = models.OneToOneField(
            User,
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
    position = models.BooleanField(
            required=False,
        )


class Attendance(models.Model):
    member = models.ForeignKey(
            Profile,
            on_delete=models.CASCADE,
            related_name='member_info',
        )
    attendance_check = models.BooleanField(
            required=False,
        )
    attendance_date = models.DateTimeField(
            auto_now_add=True,
            verbose_name='attendance date',
        )


class Absence(models.Model):
    attendance = models.ForeignKey(
            Attendance,
            on_delete=models.CASCADE,
            related_name='attendance',
        )
    minus = models.IntegerField(
            default=0,
        )
    minus_reason = models.CharField(
            max_length=100,
            verbose_name='minus reason',
        )
