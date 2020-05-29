from django.urls import path
from replays import views

urlpatterns = [
    path('', views.replay_list, name="replays"),
    path('upload', views.upload_replay, name="upload"),
]
