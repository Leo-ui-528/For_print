# Generated by Django 3.2.18 on 2023-02-28 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0016_alter_upload_type_paper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='number_of_instances',
            field=models.IntegerField(max_length=4, null=True, verbose_name='Кол-во экземпляров'),
        ),
    ]
