from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import UploadForm
from .models import Replay

def replay_list(request):
    if request.method == 'GET':
        replays = Replay.objects.all()
        return compose_page(
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
    return compose_page(
        request, 
        'replays/upload.html', 
        {
            'form': form
        }
    )

def compose_page(request, template, context):
    header = loader.render_to_string("replays/header.html")
    footer = loader.render_to_string("replays/footer.html")
    content = loader.render_to_string(template, context)

    return render(request, 'replays/page.html', {
        "header": header,
        "content": content,
        "footer": footer
    })
