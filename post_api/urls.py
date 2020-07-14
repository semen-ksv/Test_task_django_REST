from django.urls import path
from .views import PostView, PostDetailView

urlpatterns = [
    path('', PostView.as_view()),
    path('<slug>/', PostDetailView.as_view()),
]