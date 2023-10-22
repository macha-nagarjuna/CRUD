from django.urls import path
from home import views

urlpatterns = [
    path('add/', views.add_patient, name='add_patient'),
    path('display/', views.display_patients, name='display_patients'),
    path('edit/<int:id>/', views.edit_patient, name='edit_patient'),
    # Confirm delete patient view
    path('confirm_delete_patient/<int:id>/', views.confirm_delete_patient, name='confirm_delete_patient'),
    path('delete/<int:id>/', views.delete_patient, name='delete_patient'),
]
