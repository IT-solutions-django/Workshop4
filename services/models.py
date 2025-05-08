from django.db import models
from django.urls import reverse


class Service(models.Model):
    name = models.CharField('Название', max_length=255)
    subtitle = models.CharField('Подзаголовок', max_length=255)
    description = models.TextField('Описание в списке услуг')
    description_detail = models.TextField('Описание в карточке услуги')
    label = models.TextField('Подпись в карточке услуги')
    image = models.FileField('Изображение', upload_to='services/')
    is_image_small = models.BooleanField('Маленькое изображение в списке услуг?', default=False)
    slug = models.SlugField('Ссылка', max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('services:service_detail', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class ServiceStage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга', null=True, blank=True, related_name='stages')
    name = models.CharField('Название этапа', max_length=255)
    label = models.CharField('Подпись')
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Этап работы'
        verbose_name_plural = 'Этапы работы'


class TaskExample(models.Model):
    name = models.CharField('Название', max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга', null=True, blank=True, related_name='task_examples')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пример задачи'
        verbose_name_plural = 'Примеры задач'