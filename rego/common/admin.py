from django.contrib import admin
from .models import Plans, PlanFeatures, Questions


@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'price', 'periodicity')

@admin.register(PlanFeatures)
class PlanFeaturesAdmin(admin.ModelAdmin):
    list_display = ('plan', 'feature_description', 'is_active')


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')