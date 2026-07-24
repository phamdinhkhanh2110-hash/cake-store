from django.db import models

# Create your models here.
class SystemConfig(models.Model):
    config_id = models.AutoField(primary_key=True)
    config_key = models.CharField(max_length=100, unique=True)
    config_value = models.CharField(max_length=500)
    description = models.CharField(max_length=500, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        db_table = 'system_config'
 
    def __str__(self):
        return self.config_key
