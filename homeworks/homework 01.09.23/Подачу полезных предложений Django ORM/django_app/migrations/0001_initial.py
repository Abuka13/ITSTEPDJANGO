# Generated by Django 4.2.4 on 2023-08-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=300, verbose_name='Имя')),
                ('title', models.CharField(max_length=300, verbose_name='Наименование')),
                ('image', models.ImageField(upload_to='static/posts', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
        ),
    ]
