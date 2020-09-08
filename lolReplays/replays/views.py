from django.shortcuts import render, get_object_or_404
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
                'replays': replays[1:],
                'latest': replays[0]
            }
        )

def replay_detail(request, pk):
    if request.method == 'GET':
        replay = get_object_or_404(Replay, pk=pk)
        return compose_page(
            request,
            'replays/replay.html',
            {
                'replay': replay,
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
            return HttpResponseRedirect("/replay/"+str(replay.pk))
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
    content = loader.get_template(template).render(context, request)

    return render(request, 'replays/page.html', {
        "header": header,
        "content": content,
        "footer": footer
    })
