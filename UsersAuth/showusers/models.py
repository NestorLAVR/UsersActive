from django.db import models
class DayVal(models.Model):
    date = models.CharField(max_length=40, default='')
    DAU = models.CharField(max_length=10)
    MAU = models.CharField(max_length=10)
    date_day=models.CharField(max_length=40)
    date_month=models.CharField(max_length=50)
    MAUgrowth=models.CharField(max_length=10)
    DAUgrowth=models.CharField(max_length=10)
    triaMAU=models.CharField(max_length=10)
    triaDAU=models.CharField(max_length=10)
    colD=models.CharField(max_length=10)
    colM=models.CharField(max_length=10)

    def __str__(self):
        return self.date




