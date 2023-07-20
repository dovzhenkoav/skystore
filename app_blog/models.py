from django.db import models

# Create your models here.


class BlogPost(models.Model):
    name = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', null=True, blank=True)
    description = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='blog_posts/', verbose_name='превью')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликована')
    view_count = models.IntegerField(default=0, verbose_name='просмотров')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'