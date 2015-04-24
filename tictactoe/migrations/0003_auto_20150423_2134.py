# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tictactoe', '0002_game_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('message', models.CharField(max_length=200, help_text='Add a friendly message if you want', blank=True, verbose_name='Optional Message')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(related_name='invitations_sent', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(related_name='invitations_received', to=settings.AUTH_USER_MODEL, verbose_name='User to invite', help_text='Select the user with who you want to play')),
            ],
        ),
        migrations.AlterModelOptions(
            name='move',
            options={'get_latest_by': 'timestamp'},
        ),
        migrations.AddField(
            model_name='move',
            name='by_first_player',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='move',
            name='timestamp',
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
    ]
