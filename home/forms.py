from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'patient_id','date_of_birth', 'contact_number','admission_date','ward_number']
