# Generated by Django 4.1.7 on 2023-02-28 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0015_alter_upload_folding'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='type_paper',
            field=models.CharField(blank=True, choices=[('Обычная', 'Обычная'), ('Плотная', 'Плотная')], max_length=64, null=True, verbose_name='Тип бумаги'),
        ),
    ]