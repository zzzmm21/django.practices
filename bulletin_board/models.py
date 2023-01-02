from django.db import models
from django.utils.timezone import now

# Create your models here.
class Bulletin(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    writeDate = models.DateTimeField(default=now, editable=False)
    name = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)

    def __str__(self):
        return  self.title

