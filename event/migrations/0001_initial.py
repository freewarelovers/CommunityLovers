# Generated by Django 3.1 on 2020-08-23 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='event name')),
                ('slug', models.SlugField(verbose_name='event slug')),
                ('start_at', models.DateField(verbose_name='event starting date')),
                ('postion', models.CharField(max_length=200, verbose_name='event place,  city or country')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
