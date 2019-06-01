from django import forms

from .models import Chores

class DateInput(forms.DateInput):
    input_type = 'date'

class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chores
        fields = ['name', 'expire_date', 'pay']
        labels = {'text': ''}
        widgets = {'expire_date': DateInput()}