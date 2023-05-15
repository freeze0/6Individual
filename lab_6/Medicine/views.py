from django.shortcuts import render, redirect
from django.views.generic import UpdateView
from django.urls import reverse
from .models import *
from .forms import PatientForm

def index(request):
    humans = Human.objects.all()
    doctors = Doctor.objects.all()
    apps = Appointment.objects.all()
    data = {'humans': humans, 'doctors': doctors, 'apps': apps}
    return render(request, "Medicine/index.html", data)

def create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = PatientForm()
    context = {
        'form': form
    }
    return render(request, "Medicine/create.html", context)

class PatientChange(UpdateView):
    model = Human
    template_name = 'Medicine/change.html'
    form_class = PatientForm