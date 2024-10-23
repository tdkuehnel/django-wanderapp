from django.db import models

# Create your models here.

class WanderStrecke(models.Model):
    id                      = models.AutoField('ID', primary_key=True, db_column='wst_id')
    bezeichnung             = models.CharField('Bezeichnung', max_length=512, default='<unbenannt>', db_column='wst_txt')
    beschreibung            = models.CharField('Beschreibung', max_length=8192, default='<ohne Beschreibung>', db_column='wst_bsc')
    json                    = models.FileField('JSON-Datei')
    url                     = models.CharField('Link zum Teilen auf strecken-messen.de', max_length=65536, default='<leer>', db_column='wst_url')
    bild                    = models.FileField('Bilddatei', default='wanderstrecke.jpg', upload_to='bilder_wanderstrecke')
    benutzer                = models.ForeignKey('benutzer.Benutzer', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.bezeichnung

    class Meta:
        app_label            = 'wanderstrecke'
        db_table             = 'wanderstrecke'
        verbose_name         = 'Wanderstrecke'
        verbose_name_plural  = 'Wanderstrecken'
        # unique_together = [['bezeichnung',]]
        ordering             = ['bezeichnung']

class WanderPunkt(models.Model):
    id                      = models.AutoField('ID', primary_key=True, db_column='wst_id')
    bezeichnung             = models.CharField('Bezeichnung', max_length=512, default='<unbenannt>', db_column='wpt_txt')
    beschreibung            = models.CharField('Beschreibung', max_length=8192, default='<ohne Beschreibung>', db_column='wpt_bsc')

    def __str__(self):
        return self.bezeichnung

    class Meta:
        app_label            = 'wanderstrecke'
        db_table             = 'wanderpunkt'
        verbose_name         = 'Wanderpunkt'
        verbose_name_plural  = 'Wanderpunkte'
        # unique_together = [['bezeichnung',]]
        ordering             = ['bezeichnung']
