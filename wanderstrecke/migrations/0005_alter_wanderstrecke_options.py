# Generated by Django 4.2.16 on 2024-10-23 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wanderstrecke', '0004_wanderstrecke_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wanderstrecke',
            options={'ordering': ['bezeichnung'], 'verbose_name': 'Wanderstrecke', 'verbose_name_plural': 'Wanderstrecken'},
        ),
    ]
