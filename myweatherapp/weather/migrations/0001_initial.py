# Generated by Django 4.1.7 on 2023-09-03 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.CharField(max_length=200)),
                ('icon', models.CharField(max_length=10)),
            ],
        ),
    ]
