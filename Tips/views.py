from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone

from .models import Percentage

@login_required(login_url='/login')
def dashboard(request):
    service = Percentage.objects
    context = {'service':service}
    return render(request, 'tips/dashboard.html', context)

@login_required(login_url='/login')
def tips(request):
    if request.method == 'POST':
        if (request.POST['check_amt'] and request.POST['service_lvl'] == 'Custom'):
            check = float(request.POST['check_amt'])
            tip = check * (float(request.POST['custom_percent']) / 100)
            calc = check + tip
            pay = float(calc)
            percent = str(request.POST['custom_percent']) + '%'
            service = Percentage.objects
            context = {'pay':pay, 'tip':tip, 'check':check, 'percent':percent, 'service':service}
            return render(request, 'tips/dashboard.html', context)
        elif (request.POST['check_amt'] and request.POST['service_lvl']):
            service = get_object_or_404(Percentage, pk=request.POST['service_lvl'])
            percent = service.Tip_Percent
            check = float(request.POST['check_amt'])
            tip = check * float(percent)
            calc = check + tip
            pay = float(calc)
            percent = service.percent
            service = Percentage.objects
            context = {'pay':pay, 'tip':tip, 'check':check, 'percent':percent, 'service':service}
            return render(request, 'tips/dashboard.html', context)
        else:
            service = Percentage.objects
            error = 'Check amount and service level are required.\\nFor custom service level, include the custom percent.'
            context = {'service':service, 'error':error}
            return render(request, 'tips/dashboard.html', context)
    else:
        return redirect('tip-dashboard')
