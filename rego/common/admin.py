from django.contrib import admin
from .models import Plans, PlanFeatures


@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'price', 'periodicity')

@admin.register(PlanFeatures)
class PlanFeaturesAdmin(admin.ModelAdmin):
    list_display = ('plan', 'feature_description', 'is_active')