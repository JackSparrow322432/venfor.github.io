from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import HttpResponse
from django_excel_to_model.views import ExcelToModelMixin
from .models import UserProfile

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})