from django.db import models

# Create your models here.
class Employee(models.Model):
    eid = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    esal = models.FloatField()
    mail = models.EmailField()

    def __str__(self):
        return self.ename