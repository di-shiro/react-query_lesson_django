from django.urls import path, include
from rest_framework import routers
from api.views import TaskViewSet, TagViewSet

router = routers.DefaultRouter()
# URL と Views との連携: ModelViewSetはここで。
router.register('tasks', TaskViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


