# Generated by Django 3.1 on 2020-08-23 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_event_creator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
