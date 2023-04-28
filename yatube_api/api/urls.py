from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('api/', include('api.urls')),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
