from django.db import models

# Create your models here.

class WanderStrecke(models.Model):
    id                      = models.AutoField('ID', primary_key=True, db_column='wst_id')
    bezeichnung             = models.CharField('Bezeichnung', max_length=512, default='<unbenannt>', db_column='wst_txt')
    json                    = models.FileField('JSON-Datei')
    
    def __str__(self):
        return self.bezeichnung

    class Meta:
        app_label            = 'wanderstrecke'
        db_table             = 'wanderstrecke'
        verbose_name         = 'WanderStrecke'
        verbose_name_plural  = 'WanderStrecken'
        # unique_together = [['bezeichnung',]]
        ordering             = ['bezeichnung']
