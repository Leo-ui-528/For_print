# Generated by Django 3.2.18 on 2023-03-02 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0024_alter_upload_number_of_instances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='number_of_instances',
            field=models.PositiveSmallIntegerField(default=1, null=True, verbose_name='Кол-во экземпляров'),
        ),
    ]
