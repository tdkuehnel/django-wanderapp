# Generated by Django 4.2.16 on 2024-10-22 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanderstrecke', '0003_wanderstrecke_beschreibung_wanderstrecke_bild'),
    ]

    operations = [
        migrations.AddField(
            model_name='wanderstrecke',
            name='url',
            field=models.CharField(db_column='wst_url', default='<leer>', max_length=65536, verbose_name='Link zum Teilen auf strecken-messen.de'),
        ),
    ]
