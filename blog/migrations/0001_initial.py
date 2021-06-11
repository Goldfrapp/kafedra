# Generated by Django 3.2.3 on 2021-06-11 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='Название')),
                ('url', models.SlugField(max_length=255, unique=True, verbose_name='Ссылка')),
            ],
        ),
    ]
