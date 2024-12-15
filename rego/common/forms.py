from django.forms import ModelForm
from .models import Contactinfo, Questions, Plans, PlanFeatures

class ContactForm(ModelForm):
    class Meta:
        model = Contactinfo
        fields = "__all__"

class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = "__all__"

class PlanForm(ModelForm):
    class Meta:
        model = Plans
        fields = "__all__"

class PlanFeatureForm(ModelForm):
    class Meta:
        model = PlanFeatures
        fields = "__all__"