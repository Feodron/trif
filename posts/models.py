from django.db import models


# Create your models here.


class Posts(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateField('Дата поста')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/posts/{self.id}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'