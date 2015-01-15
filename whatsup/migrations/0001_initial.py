# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('usermodule', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatsUpActions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_text', models.CharField(max_length=32)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WhatsUpData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('whats_up_text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('json_data', jsonfield.fields.JSONField(default={}, blank=True)),
                ('action_id', models.ForeignKey(to='whatsup.WhatsUpActions')),
                ('user_id', models.ForeignKey(to='usermodule.PodUser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
