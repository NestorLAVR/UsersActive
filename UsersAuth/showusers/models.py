from django.db import models
class DayVal(models.Model):
    DAU = models.IntegerField()
    MAU = models.IntegerField()
    date_day=models.CharField(max_length=40)
    date_month=models.CharField(max_length=50)
    MAUgrowth=models.IntegerField()
    DAUgrowth=models.IntegerField()
    trMAU=models.CharField(max_length=10)
    trDAU=models.CharField(max_length=10)
    colD=models.CharField(max_length=10)
    colM=models.CharField(max_length=10)


    #"DAU": DAU, "MAU": MAU, "date_day": date_day, "date_month": date_month, "MAUgrowth": MAUgrowth, "DAUgrowth": DAUgrowth, "trMAU": tria_MAU, "trDAU": tria_DAU, "CD": colD, "CM": colM


