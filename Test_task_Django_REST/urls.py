from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as swagger_urls
from post_api.views import SimpleUserListCreateView, SimpleUserDetailView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/post/', include('post_api.urls')),
    path('user/', SimpleUserListCreateView.as_view()),
    path('user/<int:pk>/', SimpleUserDetailView.as_view()),
]

urlpatterns += swagger_urls

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns