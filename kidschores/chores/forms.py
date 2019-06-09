from django import forms
from crispy_forms.helper import FormHelper
from .models import Chores

class DateInput(forms.DateInput):
    input_type = 'date'

class ChoreForm(forms.ModelForm):


    class Meta:
        model = Chores
        fields = ['name', 'expire_date', 'pay']
        labels = {'text': ''}
        widgets = {'expire_date': DateInput()}

class CompleteForm(forms.ModelForm):
    class Meta:
        model = Chores
        fields = ['completed', 'image']

class ApproveForm(forms.ModelForm):
    class Meta:
        model = Chores
        fields = ['approved']