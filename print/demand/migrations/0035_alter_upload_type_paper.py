# Generated by Django 3.2.18 on 2023-05-11 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0034_upload_cuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='type_paper',
            field=models.CharField(blank=True, choices=[('Обычная', 'Обычная'), ('Плотная', 'Плотная')], max_length=64, null=True, verbose_name='Тип бумаги'),
        ),
    ]
