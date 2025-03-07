from django.shortcuts import render, redirect
from .models import Registration
import uuid
from .utils import generate_qr_code, mail
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def register(request):
    if request.method == 'POST':
        enrollment = request.POST.get('enrollment')
        name = request.POST.get('name')
        email = request.POST.get('email')
        unique_id=uuid.uuid4().hex

        # Create a new registration object
        registration = Registration(
            user = request.user,
            enrollment = enrollment,
            name=name,
            email=email,
            qr_code=f'qr_codes/{unique_id}.png',
            unique_id=unique_id
        )
        registration.save()
        generate_qr_code(unique_id)
        mail(registration)
        return redirect('pass_detail', unique_id=unique_id)

    return render(request, 'registration/register.html')

def thank_you(request):
    return render(request, 'registration/thank_you.html')

def approved_users(request):
    users = Registration.objects.all().order_by("name")
    return render(request, 'registration/approved_users.html', {'users':users})


def pass_detail(request, unique_id):
    entry_pass = Registration.objects.filter(unique_id=unique_id).first()
    return render(request, 'pass/pass_detail.html', {"entry_pass": entry_pass})

def validate(request, unique_id):
    entry_pass = Registration.objects.filter(unique_id=unique_id).first()
    if entry_pass.is_used:
        return render(request, 'pass/invalid.html')
    else:
        entry_pass.is_used = True
        entry_pass.save()
        return render(request, 'pass/valid.html')