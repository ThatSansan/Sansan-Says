# Generated by Django 2.2.4 on 2019-12-18 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_count',
        ),
        migrations.RemoveField(
            model_name='post',
            name='view_count',
        ),
    ]
