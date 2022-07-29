# Generated by Django 3.1.6 on 2022-07-27 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220727_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default='', max_length=30),
        ),
    ]
