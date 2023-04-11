from django.db import models


class Upload(models.Model):

    FORMAT = [
        ('A4', 'A4'),
        ('A3', 'A3'),
        ('A2', 'A2'),
        ('A1', 'A1'),
        ('A0', 'A0'),
    ]

    TYPE = [
        ('Обычная', 'Обычная'),
        ('Плотная', 'Плотная')
    ]

    FOLDING = [
        ('A3', 'А3'),
        ('A4', 'А4')
    ]
    STATUS = [
        ('No', 'No'),
        ('Yes', 'Yes')
    ]

    upload_file = models.FileField(verbose_name='Перетащите файл')
    file = models.FileField(verbose_name='Перетащите файл', null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    type_paper = models.CharField(max_length=64, verbose_name='Тип бумаги', null=True, choices=TYPE, blank=True)
    print_format = models.CharField(max_length=64, verbose_name='Формат печати', null=True,   choices=FORMAT, default='A3')
    folding = models.CharField(max_length=64, verbose_name='Фальцевание', null=True, choices=FOLDING, blank=True)
    number_of_instances = models.PositiveSmallIntegerField(default=1, verbose_name='Кол-во экземпляров', null=True)
    phone = models.IntegerField(verbose_name='Телефон', null=True)
    bool = models.BooleanField(default=False, verbose_name='Да/Нет', null=True)

    def __str__(self):
        return self.type_paper






