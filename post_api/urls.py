from django.urls import path
from .views import PostView, PostDetailView, PostCreateView, \
    PostUpdateView, PostDeleteView, PostAddLikeView, PostRemoveLikeView, \
    DayLikeAnalyticsView, RangeDaysLikeAnalyticsView

urlpatterns = [
    path('', PostView.as_view(), name='all-post'),
    path('create/', PostCreateView.as_view(), name="post-create"),
    path('analytics/date_<str:slug>/', DayLikeAnalyticsView.as_view(), name='day-analytic'),
    path('analytics/date-from_<str:slug1>-date-to_<str:slug2>/',
         RangeDaysLikeAnalyticsView.as_view(), name='days-analytics'),
    path('<str:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('<str:slug>/like/', PostAddLikeView.as_view(), name='add-like'),
    path('<str:slug>/unlike/', PostRemoveLikeView.as_view(), name='delete-like'),
    path('<str:slug>/update/', PostUpdateView.as_view(), name='post-update'),
    path('<str:slug>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

