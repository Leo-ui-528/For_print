# Generated by Django 4.1.7 on 2023-02-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demand', '0004_upload_bool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='bool',
            field=models.BooleanField(null=True, verbose_name='Да/Нет'),
        ),
    ]
