# Generated by Django 2.1.7 on 2019-03-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('rating', models.FloatField(default=0, verbose_name='Rating')),
                ('url', models.URLField(verbose_name='URL Adress')),
            ],
        ),
    ]
