# Generated by Django 3.1 on 2020-08-23 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_communityowner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'verbose_name': 'Community', 'verbose_name_plural': 'Communitys'},
        ),
        migrations.AlterModelOptions(
            name='communityowner',
            options={'verbose_name': 'Community owner', 'verbose_name_plural': 'Community owners'},
        ),
    ]
