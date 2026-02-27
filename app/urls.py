from django.urls import path
from .views import home,register,login,login_validation,doctorsDashboard,patientsDashboard,apptBookingByPatient,patientAppts,patient_profile_create,patient_profile_delete
urlpatterns=[
    path("",home),
    path("register/",register),
    path("login/",login),
    path("login_validation/",login_validation),
    path("doctorsDashboard/<int:id>/" ,doctorsDashboard),
    path("doctorsDashboard/<int:id>/appointments" ,doctorsDashboard),
    path("doctorsDashboard/<int:id>/profile" ,doctorsDashboard),
    path("patientsDashboard/<int:id>/" ,patientsDashboard),
    path("patientsDashboard/<int:id>/appointments" ,patientsDashboard),
    path("patientsDashboard/<int:id>/appointments/book_appt/" ,apptBookingByPatient,name="book_appt"),
    # path("patientsDashboard/<int:id>/appointments/book_appt/confirm_booking" ,confirm_booking,name="confirm_booking"),
    path("patientsDashboard/<int:id>/appointments/my_appts/" ,patientAppts,name="my_appts"),
    path("patientsDashboard/<int:id>/profile/" ,patientsDashboard),
    path("patientsDashboard/<int:id>/profile/create/",patient_profile_create),
    path("patientsDashboard/<int:id>/profile/delete/",patient_profile_delete,name="delete")
]