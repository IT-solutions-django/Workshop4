from django.db import models
from django.urls import reverse


class ArticleCategory(models.Model):
    name = models.CharField('Название', max_length=255)
    slug = models.SlugField('Ссылка', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория статьи'
        verbose_name_plural = 'Категории статей'

    def get_absolute_url(self):
        return reverse('blog:category', kwargs={'slug': self.slug})



class Article(models.Model):
    name = models.CharField('Название', max_length=255)
    subtitle = models.CharField('Подзаголовок', max_length=255)
    content = models.TextField('Контент')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    slug = models.SlugField('Ссылка', unique=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='blog/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'slug': self.slug})
