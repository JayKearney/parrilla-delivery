from .models import Reservation
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReserveTableForm

from reservation.models import Reservation

def reserve_table(request):
    reserve_form = ReserveTableForm()

    if request.method == 'POST' :
        reserve_form = ReserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
            messages.success(request, "Thank you for making your reservation. We will be in contact to confirm your booking.")
        
        # return redirect('/')


    context = {'form' : reserve_form}

    return render(request , 'Reservation/reservation.html' , context)