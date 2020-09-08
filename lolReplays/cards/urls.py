from django.urls import path
from replays import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('<str:room>/', TemplateView.as_view(template_name="index.html")),
]

