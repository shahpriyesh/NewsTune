# Generated by Django 2.2.2 on 2019-07-18 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.TextField(),
        ),
    ]
