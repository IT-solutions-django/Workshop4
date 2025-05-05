from django.db import models


class Service(models.Model):
    name = models.CharField('Название', max_length=255)
    subtitle = models.CharField('Подзаголовок', max_length=255)
    description = models.TextField('Описание')
    image = models.FileField('Изображение', upload_to='services/')
    is_image_small = models.BooleanField('Маленькое изображение?', default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class TaskExample(models.Model):
    name = models.CharField('Название', max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга', null=True, blank=True, related_name='task_examples')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Пример задачи'
        verbose_name_plural = 'Примеры задач'