from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UploadForm
from .models import Replay

def replay_list(request):
    if request.method == 'GET':
        replays = Replay.objects.all()
        return render(
            request, 
            'replays/replays.html', 
            {
                'replays': replays,
            }
        )

def upload_replay(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            replay = Replay.objects.create(
                summoner=request.POST['summoner'],
                title=request.POST['title'],
                replay=request.FILES['replay']
            )
            return HttpResponseRedirect(replay.replay.url)
    else:
        form = UploadForm()
    return render(request, 'replays/upload.html', {'form': form})