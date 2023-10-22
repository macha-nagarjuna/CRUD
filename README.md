# CRUD
django-admin startproject hospital_management_project
cd hospital_management_project
python manage.py startapp hospital_management
Define the Hospital model with the required fields (first_name, last_name, patient_id, date_of_birth, contact_number,admission_date,ward_number) in the models.py file of the hospital_management app.
python
Copy code
hospital_management/models.py

Create and apply database migrations to update the database schema.
bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a Django form for adding and editing em in the forms.py file of the _management app.
python
Copy code
hospital_management/forms.py

Create views for adding, displaying, editing, and deleting patients in the views.py file of the hospital_management app. Ensure you handle the unique constraints for email and patient_id.
python
Copy code
Hospital_management/views.py

Create templates for the HTML forms and views to interact with the user. Create HTML templates for adding (add_patient.html), displaying (display_patient.html), and editing (edit_patient.html) employee records. You can also create a base template that includes common elements.

Define the URL patterns for your views in the urls.py file of the hospital_management app.

python
Copy code
# hospital_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('display/', views.display_patient, name='display_patient'),
    path('edit/<int:id>/', views.edit_patient, name='edit_patient'),
    path('delete/<int:id>/', views.delete_patient, name='delete_patient'),
]
Include the Hospital_management app's URL patterns in the project's urls.py file.
python
Copy code
# Hospital_management_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital_management.urls')),
]
Run the development server.
bash
Copy code
python manage.py runserver
