# Generated by Django 4.1.7 on 2023-04-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='static//img', verbose_name='Фото'),
        ),
    ]
