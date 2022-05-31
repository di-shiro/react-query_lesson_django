from .models import Task, Tag
from rest_framework import viewsets
from .serializers import TaskSerializer, TagSerializer



# ModelViewSetを継承して、全てのCRUD操作を扱えるようにする。
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()    # DBから全てのTagをオブジェクトとして取得して保持しておく
    serializer_class = TagSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

