from django.urls import path
from .views import PostView, PostDetailView, PostCreateView, PostUpdateView

urlpatterns = [
    path('', PostView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<slug>/', PostDetailView.as_view()),
    path('<slug>/update', PostUpdateView.as_view()),

]