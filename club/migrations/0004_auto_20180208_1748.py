# Generated by Django 2.0.1 on 2018-02-08 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_auto_20180203_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]