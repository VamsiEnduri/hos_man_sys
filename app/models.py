from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phNum=models.CharField(max_length=15)
    password=models.CharField(max_length=14)
    c_password=models.CharField(max_length=14)
    role=models.CharField(max_length=15)
    spec=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.name

class Appointments(models.Model):
    patient =models.ForeignKey(
        "Patient",
        on_delete=models.CASCADE
    )

    doctor =models.ForeignKey(
        "Doctor",
        on_delete=models.CASCADE
    )

    problem=models.CharField(max_length=200)

    apt_time=models.DateTimeField()

    apt_status=models.CharField(
        max_length=20,
        choices=[
            ("pending","Pending"),("done","Done"),("Rejected","rejected")
        ],
        default="pending"
    )
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"${self.doctor.name} and ${self.patient.name}"

class Patient(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phNum=models.CharField(max_length=15)
    password=models.CharField(max_length=14)
    c_password=models.CharField(max_length=14)
    role=models.CharField(max_length=15)

    def __str__(self):
        return self.name




class PatientProfile(models.Model):
    age=models.IntegerField()
    b_group=models.CharField(max_length=10)
    address=models.TextField()
    weight=models.CharField(max_length=10)
    height=models.CharField(max_length=10)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.name