from rest_framework import serializers
from .models import Task, Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')
        ''' serializersで取り扱いたいDBのフィールド(CRUD操作を受け付ける) '''

class TaskSerializer(serializers.ModelSerializer):
    ''' DBに書き込む際、
    日時をシリアル形式から人が判別できるYMD形式にして、
    tag_id だけでなく、tag_name も保持しておきたいので、
    Tagテーブルの nameフィールドのデータを引っ張ってきて tag_name に格納する設定。
    '''
    created_at = serializers.DateTimeField(format="%Y-%m-%d T%H:%M", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d T%H:%M", read_only=True)
    tag_name = serializers.ReadOnlyField(source='tag.name', read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at', 'updated_at', 'tag', 'tag_name')

