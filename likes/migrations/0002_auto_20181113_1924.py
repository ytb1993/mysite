# Generated by Django 2.0 on 2018-11-13 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likecount',
            old_name='like_num',
            new_name='liked_num',
        ),
    ]
