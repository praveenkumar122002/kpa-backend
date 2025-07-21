from django.db import models

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=100)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()
    fields = models.JSONField()  # Stores the entire fields dict
    createdAt = models.DateTimeField(auto_now_add=True)

class BogieCheckSheet(models.Model):
    formNumber = models.CharField(max_length=100)
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()
    bogieDetails = models.JSONField()
    bogieChecksheet = models.JSONField()
    bmbcChecksheet = models.JSONField()
    createdAt = models.DateTimeField(auto_now_add=True)
