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
        return reverse('blog:blog_category', kwargs={'category_slug': self.slug})



class Article(models.Model):
    class RegionCodeChoices(models.TextChoices): 
        MOW = "RU-MOW", 'Москва'
        SPE = "RU-SPE", 'Санкт-Петербург'
        NEN = "RU-NEN", 'Ненецкий АО'
        YAR = "RU-YAR", 'Ярославская область'
        CHE = "RU-CHE", 'Челябинская область'
        ULY = "RU-ULY", 'Ульяновская область'
        TYU = "RU-TYU", 'Тюменская область'
        TUL = "RU-TUL", 'Тульская область'
        SVE = "RU-SVE", 'Свердловская область'
        RYA = "RU-RYA", 'Рязанская область'
        ORL = "RU-ORL", 'Орловская область'
        OMS = "RU-OMS", 'Омская область'
        NGR = "RU-NGR", 'Новгородская область'
        LIP = "RU-LIP", 'Липецкая область'
        KRS = "RU-KRS", 'Курская область'
        KGN = "RU-KGN", 'Курганская область'
        KGD = "RU-KGD", 'Калининградская область'
        IVA = "RU-IVA", 'Ивановская область'
        BRY = "RU-BRY", 'Брянская область'
        AST = "RU-AST", 'Астраханская область'
        KHA = "RU-KHA", 'Хабаровский край'
        CE = "RU-CE", 'Чеченская Республика'
        UD = "RU-UD", 'Удмуртская Республика'
        SE = "RU-SE", 'Республика Северная Осетия — Алания'
        MO = "RU-MO", 'Республика Мордовия'
        KR = "RU-KR", 'Республика Карелия'
        KL = "RU-KL", 'Республика Калмыкия'
        IN = "RU-IN", 'Республика Ингушетия'
        AL = "RU-AL", 'Республика Алтай'
        BA = "RU-BA", 'Республика Башкортостан'
        AD = "RU-AD", 'Республика Адыгея'
        CR = "RU-CR", 'Республика Крым'
        SEV = "RU-SEV", 'Севастополь'
        KO = "RU-KO", 'Республика Коми'
        KIR = "RU-KIR", 'Кировская область'
        PNZ = "RU-PNZ", 'Пензенская область'
        TAM = "RU-TAM", 'Тамбовская область'
        MUR = "RU-MUR", 'Мурманская область'
        LEN = "RU-LEN", 'Ленинградская область'
        VLG = "RU-VLG", 'Вологодская область'
        KOS = "RU-KOS", 'Костромская область'
        PSK = "RU-PSK", 'Псковская область'
        ARK = "RU-ARK", 'Архангельская область'
        YAN = "RU-YAN", 'Ямало-Ненецкий АО'
        CHU = "RU-CHU", 'Чукотский АО'
        YEV = "RU-YEV", 'Еврейская автономная область'
        TY = "RU-TY", 'Республика Тыва'
        SAK = "RU-SAK", 'Сахалинская область'
        AMU = "RU-AMU", 'Амурская область'
        BU = "RU-BU", 'Республика Бурятия'
        KK = "RU-KK", 'Республика Хакасия'
        KEM = "RU-KEM", 'Кемеровская область'
        NVS = "RU-NVS", 'Новосибирская область'
        ALT = "RU-ALT", 'Алтайский край'
        DA = "RU-DA", 'Республика Дагестан'
        STA = "RU-STA", 'Ставропольский край'
        KB = "RU-KB", 'Кабардино-Балкарская Республика'
        KC = "RU-KC", 'Карачаево-Черкесская Республика'
        KDA = "RU-KDA", 'Краснодарский край'
        ROS = "RU-ROS", 'Ростовская область'
        SAM = "RU-SAM", 'Самарская область'
        TA = "RU-TA", 'Республика Татарстан'
        ME = "RU-ME", 'Республика Марий Эл'
        CU = "RU-CU", 'Чувашская Республика'
        NIZ = "RU-NIZ", 'Нижегородская область'
        VLA = "RU-VLA", 'Владимирская область'
        MOS = "RU-MOS", 'Московская область'
        KLU = "RU-KLU", 'Калужская область'
        BEL = "RU-BEL", 'Белгородская область'
        ZAB = "RU-ZAB", 'Забайкальский край'
        PRI = "RU-PRI", 'Приморский край'
        KAM = "RU-KAM", 'Камчатский край'
        MAG = "RU-MAG", 'Магаданская область'
        SA = "RU-SA", 'Республика Саха (Якутия)'
        KYA = "RU-KYA", 'Красноярский край'
        ORE = "RU-ORE", 'Оренбургская область'
        SAR = "RU-SAR", 'Саратовская область'
        VGG = "RU-VGG", 'Волгоградская область'
        VOR = "RU-VOR", 'Воронежская область'
        SMO = "RU-SMO", 'Смоленская область'
        TVE = "RU-TVE", 'Тверская область'
        PER = "RU-PER", 'Пермский край'
        KHM = "RU-KHM", 'Ханты-Мансийский АО - Югра'
        TOM = "RU-TOM", 'Томская область'
        IRK = "RU-IRK", 'Иркутская область'
        HR = "RU-HR", 'Херсонская область'
        ZP = "RU-ZP", 'Запорожская область'
        DON = "RU-DON", 'Донецкая Народная Республика'
        LUG = "RU-LUG", 'Луганская Народная Республика'

    name = models.CharField('Название', max_length=255)
    subtitle = models.CharField('Подзаголовок', max_length=255)
    content = models.TextField('Контент')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    slug = models.SlugField('Ссылка', unique=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, related_name='articles')
    image = models.ImageField('Изображение', upload_to='blog/')
    services = models.ManyToManyField('services.Service', verbose_name='Услуги', related_name='articles')
    is_popular = models.BooleanField('Популярная', default=False)
    region_code = models.CharField('Регион', null=True, blank=True, choices=RegionCodeChoices.choices)

    map_card_label = models.CharField('Подпись в карточке на карте', help_text='Пример: "новый стандарт урбанизма"', null=True, blank=True)
    year = models.IntegerField('Год', null=True, blank=True) 
    city = models.CharField('Город', help_text='Пример: "Владивосток"', null=True, blank=True, max_length=50) 
    square = models.CharField('Площадь', help_text='Пример: "20 тыс м2"', null=True, blank=True, max_length=50)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def get_absolute_url(self):
        return reverse('blog:article', kwargs={'slug': self.slug})
