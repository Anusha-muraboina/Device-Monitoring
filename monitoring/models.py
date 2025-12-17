from django.db import models
class Device(models.Model):
    name=models.CharField(max_length=200,unique=True)
    location=models.CharField(max_length=200,blank=True,null=True)
class Reading(models.Model):
    device=models.ForeignKey(Device,on_delete=models.CASCADE,related_name='readings')
    timestamp=models.DateTimeField()
    power=models.FloatField()
    status=models.CharField(max_length=10)
    class Meta:
        unique_together=('device','timestamp')
        ordering=['-timestamp']
