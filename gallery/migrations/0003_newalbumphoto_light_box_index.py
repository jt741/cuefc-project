# Generated by Django 2.2.12 on 2020-08-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_newalbum_newalbumphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='newalbumphoto',
            name='light_box_index',
            field=models.IntegerField(default=1),
        ),
    ]
