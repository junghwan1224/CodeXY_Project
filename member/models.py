from django.db import models
# from django.contrib.auth.models import User
from club.models import Club
from django.conf import settings
# Create your models here.


class Profile(models.Model):
    # club = models.ManyToManyField(
    #         Club,
    #         related_name='club_profile',
    #     )
    user = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
        )
    school = models.CharField(
            max_length=20,
            verbose_name='member school',
        )
    phone_number = models.CharField(
            max_length=20,
            verbose_name='phone number',
        )


class Member(models.Model):
    club = models.ForeignKey(
            Club,
            on_delete=models.CASCADE,
            related_name='club_member',
        )
    member = models.ForeignKey(
            Profile,
            on_delete=models.CASCADE,
            related_name='user_profile',
        )


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
