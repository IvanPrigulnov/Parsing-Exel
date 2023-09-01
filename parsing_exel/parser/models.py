from django.db import models


class Billboards(models.Model):
    LIGHTING = ['Да', 'Нет']
    PRODUCT_RESTRICTIONS = ['Алкогольные напитки',
                            'Табачные изделия,Алкогольные напитки']

    city = models.CharField(db_column='Города', max_length=20, verbose_name='Город')
    surface_type = models.CharField(db_column='Тип поверхности', max_length=50, verbose_name='Тип поверхности')
    lighting = models.CharField(db_column='Осв', max_length=3, choices=LIGHTING, verbose_name='Освещение')
    address = models.CharField(db_column='Адрес', max_length=250, verbose_name='Адрес')
    latitude = models.FloatField(db_column='Широта', verbose_name='Широта')
    longitude = models.FloatField(db_column='Долгота', verbose_name='Долгота')
    product_restrictions = models.CharField(db_column='Ограничения по продукту', null=True, max_length=40, choices=PRODUCT_RESTRICTIONS, verbose_name='Ограничения по продукту')
    district = models.CharField(db_column='Городской округ', null=True, max_length=100, verbose_name='Городской округ')
    permission = models.DateField(db_column='Разрешение ПО', null=True, verbose_name='Разрешение ПО')
    date_create = models.DateTimeField(db_column='Дата создания', auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(db_column='Дата обновления', auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f'{self.city} {self.address}'

    class Meta:
        db_table = 'Билборды'
        verbose_name = 'Билборды'
        verbose_name_plural = 'Билборды'
        indexes = [
            models.Index(fields=['city', 'address'], name='address_idx'),
            models.Index(fields=['permission'], name='permission_idx'),
        ]
        unique_together = [
            ['city', 'address'],
            ['latitude', 'longitude']
        ]