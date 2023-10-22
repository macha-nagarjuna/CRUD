from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm

def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_patients')
    else:
        form = PatientForm()
    return render(request, 'add_patient.html', {'form': form})

def display_patients(request):
    patients = Patient.objects.all()
    return render(request, 'display_patients.html', {'patients': patients})

def edit_patient(request, id):
    patients = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patients)
        if form.is_valid():
            form.save()
            return redirect('display_patients')
    else:
        form = PatientForm(instance=patients)
    return render(request, 'edit_patient.html', {'form': form, 'patients': patients})

def confirm_delete_patient(request, id):
    patients = get_object_or_404(Patient, id=id)
    return render(request, 'confirm_delete_patient.html', {'patients': patients})

def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return redirect('display_patients')