from django import forms

from replays.models import Replay

class UploadForm(forms.Form):

    summoner = forms.CharField(
        max_length=50
    )

    title = forms.CharField(
        max_length=75
    )

    replay = forms.FileField()
