from django.db import models

# Create your models here.
class Plans(models.Model):
    class PeriodicityChoice(models.TextChoices):
        MONTH = 'Month',
        YEAR = 'Year'
    plan_name = models.CharField(max_length=10)
    price = models.FloatField()
    periodicity = models.CharField(max_length=20, choices=PeriodicityChoice, default=PeriodicityChoice.MONTH)

    def __str__(self):
        return self.plan_name
    
class PlanFeatures(models.Model):
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE)
    feature_description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.feature_description}-feature"


