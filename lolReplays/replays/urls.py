from django.urls import path
from replays import views

urlpatterns = [
    path('', views.replay_list, name="replays"),
    path('replay/<int:pk>', views.replay_detail, name="replay"),
    path('upload/', views.upload_replay, name="upload"),
]
