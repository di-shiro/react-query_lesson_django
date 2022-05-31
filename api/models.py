from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)     # Tagの名前

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100)                # Task名
    created_at = models.DateTimeField(auto_now_add=True)    # 新規追加された時の日時
    updated_at = models.DateTimeField(auto_now=True)      # 更新される度に更新日時を上書き
    tag = models.ForeignKey(
        Tag,        # One to One (一対多)の関係で Tag と紐付ける。
        null=True,  # Tag がない場合もあるので Null になることも許可する
        on_delete=models.CASCADE)   # Taskに紐付いたTagが削除された時、芋づる式に連動してTaskも削除する。

    def __str__(self):
        return self.title

