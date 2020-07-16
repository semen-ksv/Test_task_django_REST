from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as swagger_urls
from post_api.views import SimpleUserListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('djoser.urls')),
    path('api/post/', include('post_api.urls')),
    path('user/', SimpleUserListView.as_view()),
]

urlpatterns += swagger_urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns