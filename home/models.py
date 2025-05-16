from django.db import models


class CompanyInfo(models.Model): 
    description = models.TextField('Описание', max_length=3000)
    description_label = models.TextField('Подпись под описанием', max_length=1000)
    whatsapp_link = models.URLField('Ссылка на WhatsApp', max_length=200, null=True, blank=True)
    telegram_link = models.URLField('Ссылка на Telegram', max_length=200, null=True, blank=True)
    vk_link = models.URLField('Ссылка на Вконтакте', max_length=200, null=True, blank=True)
    phone = models.CharField('Номер телефона', max_length=20, null=True, blank=True)
    email = models.EmailField('Email', null=True, blank=True, max_length=100)
    address = models.CharField('Адрес', max_length=150, default='690065, Приморский край, г. Владивосток, ул. Пушкина 91')
    work_hours = models.CharField('Время работы', max_length=100, default='пн-пт 08:30–17:30')

    privacy_policy = models.FileField('Политика конфиденциальности', upload_to='privacy_policy', null=True, blank=True)

    plan_file = models.FileField('План работ', upload_to='home/company_info/', null=True, blank=True)
    necessary_data_file = models.FileField('Перечень необходимых данных', upload_to='home/company_info/', null=True, blank=True)

    class Meta: 
        verbose_name = 'Информация о компании'
        verbose_name_plural = 'Информация о компании'

    def __str__(self):
        return 'Информация о компании'
    
    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls) -> "CompanyInfo":
        instance, created = cls.objects.get_or_create(id=1)
        return instance