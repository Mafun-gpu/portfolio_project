# Generated by Django 5.1.6 on 2025-03-22 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='category',
            field=models.CharField(choices=[('MUSIC', 'Music'), ('SPORT', 'Sport'), ('FILM', 'Film'), ('OTHER', 'Other')], default='OTHER', max_length=50, verbose_name='Категория'),
        ),
    ]
