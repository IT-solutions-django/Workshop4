from django.db import models


class Quote(models.Model): 
    text = models.CharField('Текст', max_length=500) 
    author_name = models.CharField('Имя автора', max_length=100)
    author_position = models.CharField('Должность автора', max_length=100) 
    author_photo = models.ImageField('Фото автора', upload_to='contacts/quotes/') 

    class Meta: 
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитаты' 

    def __str__(self): 
        return f'{self.author_name}: "{self.text}"'
    

class Review(models.Model): 
    name = models.CharField('Название', max_length=100) 
    text = models.CharField('Текст', max_length=500) 
    rating = models.SmallIntegerField('Оценка (от 1 до 5)', default=5)
    author_name = models.CharField('Имя автора', max_length=100)
    author_company = models.CharField('Должность автора', max_length=100) 

    class Meta: 
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы' 

    def __str__(self): 
        return f'{self.author_name}: "{self.name}"'
    

class Partner(models.Model): 
    name = models.CharField('Название', max_length=50) 
    logo = models.FileField('Логотип', upload_to='contacts/partners/')

    class Meta: 
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры' 

    def __str__(self): 
        return f'{self.name}'
    

class Worker(models.Model): 
    name = models.CharField('Имя', max_length=100) 
    position = models.CharField('Должность', max_length=100) 
    photo = models.ImageField('Фото', upload_to='contacts/workers/')

    class Meta: 
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники' 

    def __str__(self): 
        return f'{self.name}'


class Request(models.Model):
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=100)
    message = models.TextField('Сообщение', null=True, blank=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_processed = models.BooleanField('Обработано', default=False)

    def __str__(self):
        return f'{self.name} ({self.phone})' 

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
