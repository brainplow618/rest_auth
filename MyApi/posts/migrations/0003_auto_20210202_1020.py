# Generated by Django 3.1.5 on 2021-02-02 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_rates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postsrates',
            old_name='dislike',
            new_name='dislikes',
        ),
    ]