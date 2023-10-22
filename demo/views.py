# django-admin startproject employee_management_project
# cd employee_management_project
# python manage.py startapp employee_management
# Define the Employee model with the required fields (first_name, last_name, employee_id, email, and contact_number) in the models.py file of the employee_management app.
# python
# Copy code
# employee_management/models.py

# Create and apply database migrations to update the database schema.
# bash
# Copy code
# python manage.py makemigrations
# python manage.py migrate
# Create a Django form for adding and editing employees in the forms.py file of the employee_management app.
# python
# Copy code
# employee_management/forms.py

# Create views for adding, displaying, editing, and deleting employees in the views.py file of the employee_management app. Ensure you handle the unique constraints for email and employee_id.
# python
# Copy code
# employee_management/views.py

# Create templates for the HTML forms and views to interact with the user. Create HTML templates for adding (add_employee.html), displaying (display_employees.html), and editing (edit_employee.html) employee records. You can also create a base template that includes common elements.

# Define the URL patterns for your views in the urls.py file of the employee_management app.

# python
# Copy code
# # employee_management/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('add/', views.add_employee, name='add_employee'),
#     path('display/', views.display_employees, name='display_employees'),
#     path('edit/<int:id>/', views.edit_employee, name='edit_employee'),
#     path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
# ]
# Include the employee_management app's URL patterns in the project's urls.py file.
# python
# Copy code
# # employee_management_project/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('employee_management.urls')),
# ]
# Run the development server.
# bash
# Copy code
# python manage.py runserver