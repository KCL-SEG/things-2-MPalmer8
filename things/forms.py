"""Forms of the project."""

from django import forms

class ThingsForm(forms.Modelform):
  class Meta:
    model = Thing
    fields = ['name',]
    description = forms.Textarea(max_length=120, blank=True)
    quantity = forms.NumberInput()
