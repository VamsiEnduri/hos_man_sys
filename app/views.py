from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Doctor,Patient,Appointments,PatientProfile
from django.http import HttpResponse
from .forms import PatientProfileForm
# Create your views here.
def home(req):
    return render(req,"registration.html")

def patient_profile_delete(req,id):
    patient=Patient.objects.get(id=id)

    if req.method == "POST":
        patient.delete()
        return render(req,"patientsProfile.html")
    return HttpResponse("patient dleted")    


def patient_profile_create(req,id):
    patient=Patient.objects.get(id=id)
    form = PatientProfileForm()

    if req.method == "POST":
        pProfile=PatientProfileForm(req.POST)
        if pProfile.is_valid():
            p = pProfile.save(commit = False)
            p.patient=patient
            p.save()
    return render(req,"patient_profile_create.html",{"form":form,"user":patient})

def apptBookingByPatient(req,id):
    pat=Patient.objects.get(id=id)
    doctors = Doctor.objects.all().values()

    if req.method == "POST":

        a=req.POST.get("d_id")
        b=req.POST.get("problem")
        c=req.POST.get("datetime-local")
        print(a,b,c)

        doc=Doctor.objects.get(id=a)
        Appointments.objects.create(patient=pat,doctor=doc,problem=b,apt_time=c)

        return render(req,"book_appt.html",{"user":pat,"doctors":doctors})

    return render(req,"book_appt.html",{"user":pat,"doctors":doctors})

def patientAppts(req,id):
    patient=Patient.objects.get(id=id)
    myAppts= Appointments.objects.filter(patient_id=id)
    return  render(req,"my_appts.html",{"appts":myAppts,"user":patient})

def patientsDashboard(req,id):
    patient=Patient.objects.get(id=id) # obj :-- .
    profile=PatientProfile.objects.filter(patient_id=id).first()

    if "appointments" in req.path:
        template="patientsAppointments.html"
    elif "profile" in req.path:
        template="patientsProfile.html"
    else:
        template="patientsDashboard.html"
    return render(req,template,{"user":patient,"profile":profile})

def doctorsDashboard(req,id):
    doctor=Doctor.objects.get(id=id) # obj :-- .
    appts=Appointments.objects.filter(doctor_id=id)
    print(appts)

    if req.method == POST:
        apt_s=req.POST.get("status") # done / Done
    if "appointments" in req.path:
        template="doctorsAppointments.html"
    elif "profile" in req.path:
        template="doctorsProfile.html"
    else:
        template="DoctorsDashboard.html"
    return render(req,template,{"user":doctor,"appts":appts})


@api_view(["POST"])
def login_validation(req):
    e=req.data.get("e")
    p=req.data.get("p")
    r=req.data.get("r")
    drs=Doctor.objects.all().values()
    pts=Patient.objects.all().values()
    
    if r == "Doctor":
        print("vamsi     aaaa")
        for i in drs:
            if i["email"] == e and i["password"] == p:
                return Response({"msg":"doctor login done","r_url":"doctorsDashboard","id":i["id"],"role":i["role"]})
    elif r == "Patient":
        for i in pts:
            if i["email"] == e and i["password"] == p:
                return Response({"msg":"patient login done","r_url":"patientsDashboard","id":i["id"],"role":i["role"]})
    else:
        return Response("role doesnt exist")        


@api_view(["GET"])
def login(req):
    return render(req,"login.html")


@api_view(["POST"])
def register(req):
    n=req.data.get("n")
    e=req.data.get("e")
    ph=req.data.get("ph")
    p=req.data.get("p")
    cp=req.data.get("cp")
    r=req.data.get("r")
    s=req.data.get("s")
    if p == cp:
        if r == "Doctor":
            Doctor.objects.create(name=n,email=e,phNum=ph,password=p,c_password=cp,role=r,spec=s)
            return Response({"msg":"doctor added successfully ","d_name":n})
        
        if r == "Patient":
            Patient.objects.create(name=n,email=e,phNum=ph,password=p,c_password=cp,role=r)
            return Response({"msg":"patient added successfully ","p_name":n})

    else:
        return Response("p and cp are not matched")   
    return Response("register")