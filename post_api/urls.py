from django.urls import path
from .views import PostView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<str:slug>/', PostDetailView.as_view()),
    path('<str:slug>/update', PostUpdateView.as_view()),
    path('<str:slug>/delete', PostDeleteView.as_view()),

]