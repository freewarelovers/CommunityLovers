# Generated by Django 3.1 on 2020-09-06 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20200823_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='username'),
        ),
    ]
