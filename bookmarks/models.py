from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Book(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='books')
    url = models.URLField(verbose_name="Ссылка", blank=False, null=False)
    title = models.CharField(verbose_name="Заголовок", blank=True, null=True, max_length=255)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    favicon = models.URLField(default=None)

