# Generated by Django 2.2.12 on 2020-08-22 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20200822_1053'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.AddField(
            model_name='newalbum',
            name='show_on_website',
            field=models.BooleanField(default=True),
        ),
    ]