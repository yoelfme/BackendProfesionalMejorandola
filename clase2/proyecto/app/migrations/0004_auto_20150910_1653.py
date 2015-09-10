# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150909_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agregador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=140)),
            ],
        ),
        migrations.AlterModelOptions(
            name='enlace',
            options={'ordering': ['-votos']},
        ),
        migrations.AddField(
            model_name='agregador',
            name='enlaces',
            field=models.ManyToManyField(to='app.Enlace'),
        ),
    ]
