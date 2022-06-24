from django.db import models


class Series(models.Model):
    SeriesInstanceUID = models.CharField(max_length=200)
    PatientID = models.CharField(max_length=200)
    PatientName = models.CharField(max_length=200)
    StudyInstanceUID = models.CharField(max_length=200)
    InstancesInSeries = models.IntegerField()

    def __str__(self):
        return self.PatientName



