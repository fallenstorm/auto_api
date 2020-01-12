from django.db import models


class AutoApiModel(models.Model):
    class Meta:
        app_label = 'tests'
        abstract = True


class Smi(AutoApiModel):
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    name = models.TextField(verbose_name='Название СМИ')


class Blog(AutoApiModel):
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    name = models.TextField(verbose_name='Название блога')
    subscribers = models.IntegerField(verbose_name='Количество подписчиков')
    smi = models.ManyToManyField(Smi)


class Post(AutoApiModel):
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    text = models.TextField(verbose_name='Текст поста')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='posts')

