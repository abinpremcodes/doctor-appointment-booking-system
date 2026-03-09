from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Appointment


# @login_required
# def book_appointment(request):
#     if request.method=='POST':
#         form=AppointmentForm(request.POST)
#         if form.is_valid():
#             appointment=form.save(commit=False)
#             appointment.patient=request.user
#             appointment.save()
#             return redirect("dashboard")
#     else:
#         form=AppointmentForm()
#     return render(request,'book_appointment.html',{'form':form})

@login_required
def book_appointment(request):

    if request.user.role != "patient":
        return redirect("home")

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user
            appointment.save()
            return redirect("dashboard")
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})


# @login_required
# def dashboard(request):
#     appointments=Appointment.objects.filter(patient=request.user)
#     return render(request,'dashboard.html',{'appointments':appointments})


@login_required
def dashboard(request):

    if request.user.role == "patient":
        appointments = Appointment.objects.filter(patient=request.user)

    elif request.user.role == "doctor":
        appointments = Appointment.objects.filter(
            doctor__user=request.user
        )

    else:
        appointments = None

    return render(request, 'dashboard.html', {'appointments': appointments})




def home(request):
    return render(request,'home.html')

from .forms import RegisterForm
from django.contrib.auth import login

# def register(request):
#     if request.method=='POST':
#         form=RegisterForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             login(request,user)
#             return redirect('dashboard')
#     else:
#         form=RegisterForm()
#     return render(request,'register.html',{'form':form})

from django.contrib import messages
from django.contrib.auth import login

def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('dashboard')
        else:
            # Show errors so you know why it fails
            print(form.errors)  # DEBUG in console
            messages.error(request, "There was a problem creating your account. Check the console or fix the fields.")
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

login_required
def cancel_appointment(request,appointment_id):
    appointment=get_object_or_404(Appointment,id=appointment_id)
    if appointment.patient==request.user:
        appointment.delete()
    return redirect('dashboard')









