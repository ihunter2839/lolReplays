from django.db import models

import datetime

class Replay(models.Model):
   
    summoner = models.CharField(
        max_length=50,
        default='',
        blank=True,
        null=False
    )

    created = models.DateField(
        auto_now_add=True,
        blank=True,
    )

    title = models.CharField(
        max_length=75,
        default='',
        blank=True,
        null=False
    )

    replay = models.FileField(
        upload_to=''
    )

    class Meta:
        ordering = ('-pk',)
