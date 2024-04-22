from django.shortcuts import render
from .models import User


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(email=email).exists():
            user = User(username=username, email=email, password=password)
            user.save()
            return render(request, 'registration_success.html')
        else:
            return render(request, 'registration.html', {'error': 'User with this email already exists'})

    return render(request, 'registration.html')
