# Generated by Django 3.2.18 on 2023-03-02 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0025_alter_upload_number_of_instances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='number_of_instances',
            field=models.PositiveSmallIntegerField(choices=[('A4', 'A4'), ('A3', 'A3'), ('A2', 'A2'), ('A1', 'A1'), ('A0', 'A0')], default=1, null=True, verbose_name='Кол-во экземпляров'),
        ),
    ]
