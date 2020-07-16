from django.urls import path
from .views import PostView, PostDetailView, PostCreateView,\
    PostUpdateView,PostDeleteView, PostAddLikeView, PostRemoveLikeView,\
    DayLikeAnalyticsView, RangeDaysLikeAnalyticsView

urlpatterns = [
    path('', PostView.as_view(), name='all-post'),
    path('create/', PostCreateView.as_view(), name="post-create"),
    path('analytics/date_<slug>/', DayLikeAnalyticsView.as_view()),
    path('analytics/date-from_<slug1>-date-to_<slug2>/', RangeDaysLikeAnalyticsView.as_view()),
    path('<str:slug>/', PostDetailView.as_view()),
    path('<str:slug>/like/', PostAddLikeView.as_view()),
    path('<str:slug>/unlike/', PostRemoveLikeView.as_view()),
    path('<str:slug>/update/', PostUpdateView.as_view()),
    path('<str:slug>/delete/', PostDeleteView.as_view()),


]

# from activitylog.views import ObtainJWTView
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('login/', view=ObtainJWTView.as_view(), name='login'),
# ]