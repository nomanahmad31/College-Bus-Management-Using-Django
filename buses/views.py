from django.shortcuts import render, redirect, get_object_or_404
from .models import Bus, Pass
from users.models import User
from django.contrib import messages
from . forms import PassGenerationForm
# Create your views here.


def buses(request):
    if request.user.is_authenticated:
        all_buses = Bus.objects.all()
        context = {
            'all_buses': all_buses
        }
        return render(request, 'buses/all-buses.html', context)
    else:
        return redirect('index')


def details(request, id):
    if request.user.is_authenticated:
        bus = get_object_or_404(Bus, id=id)
        user = request.user
##        cantt = Bus.objects.filter(starting_point__iexact='Cantt')
##        station = Bus.objects.filter(starting_point__iexact='Station')
        if request.method == "POST":
            if Pass.objects.filter(user=user).exists():
                messages.error(request, "You already have a pass")
                return redirect('details', id=id)
            else:
                form = PassGenerationForm(request.user, request.POST)
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.user = request.user
                    obj.save()
                    return redirect('bus-pass')
                
        else:
            form = PassGenerationForm(request.user)
        context = {
            'bus': bus,
            'form': form,
        }
        return render(request, 'buses/details.html', context)
    else:
        return redirect('index')
