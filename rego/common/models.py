from django.db import models

class Contactinfo(models.Model):
    address = models.TextField()
    mobile_number = models.CharField(max_length=15)
    email = models.CharField(max_length=150)

# Create your models here.
class Plans(models.Model):
    class PeriodicityChoice(models.TextChoices):
        MONTH = 'Month',
        YEAR = 'Year'
    plan_name = models.CharField(max_length=50)
    price = models.FloatField()
    periodicity = models.CharField(max_length=20, choices=PeriodicityChoice, default=PeriodicityChoice.MONTH)

    def __str__(self):
        return self.plan_name


class PlanFeatures(models.Model):
    plan = models.ForeignKey(Plans, on_delete=models.CASCADE, related_name="features")
    feature_description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.feature_description}-feature"

    class Meta:
        ordering = ['-is_active']



# question models
class Questions(models.Model):
    question = models.TextField()
    answer = models.TextField()