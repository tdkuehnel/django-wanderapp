# Generated by Django 4.2.16 on 2024-10-21 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('benutzer', '0002_historicalbenutzer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='benutzer',
            options={'permissions': [('berechtigung', 'Berechtigung')], 'verbose_name': 'Benutzer', 'verbose_name_plural': 'Benutzer'},
        ),
        migrations.AlterModelOptions(
            name='historicalbenutzer',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Benutzer', 'verbose_name_plural': 'historical Benutzer'},
        ),
        migrations.AlterField(
            model_name='benutzer',
            name='email',
            field=models.EmailField(blank=True, db_column='bnz_email', default='', max_length=128, verbose_name='E-Post-Adresse'),
        ),
        migrations.AlterField(
            model_name='historicalbenutzer',
            name='email',
            field=models.EmailField(blank=True, db_column='bnz_email', default='', max_length=128, verbose_name='E-Post-Adresse'),
        ),
        migrations.AlterField(
            model_name='historicalbenutzer',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]
