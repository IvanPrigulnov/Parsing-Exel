from django.db import models


class Billboards(models.Model):
    LIGHTING = [
        ('Да', 'Да'),
        ('Нет', 'Нет')
    ]
    PRODUCT_RESTRICTIONS = [
        ('Алкогольные напитки', 'Алкогольные напитки'),
        ('Табачные изделия,Алкогольные напитки', 'Табачные изделия,Алкогольные напитки')
    ]

    city = models.CharField(db_column='Город', max_length=20, verbose_name='Город')
    surface_type = models.CharField(db_column='Тип поверхности', max_length=50, verbose_name='Тип поверхности')
    lighting = models.CharField(db_column='Осв', max_length=3, choices=LIGHTING, verbose_name='Освещение')
    address = models.CharField(db_column='Адрес', max_length=250, verbose_name='Адрес')
    latitude = models.FloatField(db_column='Широта', verbose_name='Широта')
    longitude = models.FloatField(db_column='Долгота', verbose_name='Долгота')
    product_restrictions = models.CharField(db_column='Ограничения по продукту', null=True, blank=True, max_length=40, choices=PRODUCT_RESTRICTIONS, verbose_name='Ограничения по продукту')
    district = models.CharField(db_column='Городской округ', null=True, blank=True, max_length=100, verbose_name='Городской округ')
    permission = models.DateField(db_column='Разрешение ПО', null=True, blank=True, verbose_name='Разрешение ПО')
    date_create = models.DateTimeField(db_column='Дата создания', auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(db_column='Дата обновления', auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.city}, {self.address}'

    class Meta:
        db_table = 'Билборды'
        verbose_name = 'Билборд'
        verbose_name_plural = 'Билборды'
        indexes = [
            models.Index(fields=['city', 'address'], name='address_idx'),
            models.Index(fields=['permission'], name='permission_idx'),
        ]
        unique_together = [
            ['latitude', 'longitude']
        ]


class Sides(models.Model):
    internal_code = models.CharField(db_column='Вн. код', primary_key=True, max_length=20, unique=True, verbose_name='Вн. код')
    billboard = models.ForeignKey(Billboards, db_column='ID Билборда', on_delete=models.CASCADE, verbose_name='Город/Адрес билборда')
    side = models.CharField(db_column='Сторона', max_length=6, verbose_name='Сторона')
    price = models.DecimalField(db_column='Прайс с НДС', max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Прайс с НДС')
    installation_price = models.DecimalField(db_column='Монтаж. Прайс с НДС', max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Монтаж. Прайс с НДС')
    plywood_price = models.DecimalField(db_column='Переклейка. Прайс с НДС', max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Переклейка. Прайс с НДС')
    photo_or_scheme = models.URLField(db_column='Фото/схема', verbose_name='Фото/схема')
    digital_views = models.PositiveSmallIntegerField(db_column='Диджитал кол-во показов', null=True, blank=True,  verbose_name='Диджитал кол-во показов')
    media_material = models.CharField(db_column='Материал носителя', max_length=100, null=True, blank=True, verbose_name='Материал носителя')
    technical_requirements = models.URLField(db_column='Тех. требования', null=True, blank=True, verbose_name='Тех. требования')
    note = models.TextField(db_column='Примечание', null=True, blank=True, verbose_name='Примечание')
    date_create = models.DateTimeField(db_column='Дата создания', auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(db_column='Дата обновления', auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.internal_code

    class Meta:
        db_table = 'Стороны'
        verbose_name = 'Сторону'
        verbose_name_plural = 'Стороны'
        indexes = [
            models.Index(fields=['internal_code'], name='internal_code_idx'),
        ]


class ESPAR(models.Model):
    ESPAR_code = models.CharField(db_column='Код ЭСПАР', max_length=20, verbose_name='Код ЭСПАР')
    GRP = models.FloatField()
    OTS = models.FloatField()
    side = models.ForeignKey(Sides, db_column='Вн. код стороны', on_delete=models.CASCADE, verbose_name='Вн. код стороны')
    billboard = models.ForeignKey(Billboards, db_column='ID Билборда', on_delete=models.CASCADE, verbose_name='Город/адрес билборда')
    date_create = models.DateTimeField(db_column='Дата создания', auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(db_column='Дата обновления', auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.ESPAR_code

    class Meta:
        db_table = 'ESPAR'
        verbose_name = 'ESPAR'
        verbose_name_plural = 'ESPAR'
        indexes = [
            models.Index(fields=['ESPAR_code'], name='ESPAR_code_idx'),
        ]


class Sales(models.Model):
    billboard = models.ForeignKey(Billboards, db_column='ID Билборда', on_delete=models.CASCADE, verbose_name='Город/адрес билборда')
    side = models.ForeignKey(Sides, db_column='Вн. код стороны', on_delete=models.CASCADE, verbose_name='Вн. код стороны')
    ESPAR = models.ForeignKey(ESPAR, db_column='Код ЭСПАР', on_delete=models.CASCADE, verbose_name='Код ЭСПАР')
    year = models.PositiveSmallIntegerField(db_column='Год', verbose_name='Год')
    month = models.CharField(db_column='Месяц', max_length=10, verbose_name='Месяц')
    status = models.CharField(db_column='Статус', max_length=400, null=True, blank=True, verbose_name='Статус')
    date_create = models.DateTimeField(db_column='Дата создания', auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(db_column='Дата обновления', auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.month} {self.year}-{self.status}'

    class Meta:
        db_table = 'Продажи'
        verbose_name = 'Продажу'
        verbose_name_plural = 'Продажи'
        indexes = [
            models.Index(fields=['status'], name='status_idx'),
        ]

