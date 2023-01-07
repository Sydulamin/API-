from django.db import models


# Create your models here.



class Prof(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True)
    father_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)
