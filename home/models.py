from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=5, unique=True)
    date_of_birth=models.DateField()

    contact_number = models.CharField(max_length=10)
    admission_date=models.DateField()
    ward_number=models.CharField(max_length=10)


    def _str_(self):
        return self.first_name + ' ' + self.last_name