from django import forms
from . models import Bus, Pass


class PassGenerationForm(forms.ModelForm):
    route = forms.ModelChoiceField(queryset=Bus.objects.all(), label="Routes")

    class Meta:
        model = Pass
        fields = ("route",)

    def __init__(self, user,  *args, **kwargs):
        super(PassGenerationForm, self).__init__(*args, **kwargs)
