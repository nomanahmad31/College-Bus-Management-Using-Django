from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .forms import FacultyCreationForm, StudentCreationForm
from django.contrib import messages, auth
from buses.models import Pass
from .models import User
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.http import JsonResponse

import stripe

stripe.api_key = "YOUR SECRET KEY"

# Create your views here.


def faculty_signup(request):
    if request.method == 'POST':
        form = FacultyCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            mail = form.cleaned_data.get('email')
            print(mail)
            current_site = get_current_site(request)
            mail_subject = 'SRMCEM GROUP : Dear Faculty,Activate your account.'
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })

            send_mail(mail_subject, message, 'midtownsmasher786@gmail.com', [mail])
            return render(request, 'users/email_confirmation.html')
            messages.success(request, 'Success. Now Please Login to continue')
            
            #return redirect('index')
        else:
            messages.error(request, 'Error. Please Check your form again.')
    else:
        form = FacultyCreationForm()
    return render(request, 'users/faculty-signup.html', {'form': form})


def student_signup(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            mail = form.cleaned_data.get('email')
            print(mail)
            current_site = get_current_site(request)
            mail_subject = 'SRMCEM GROUP : Dear Student,Activate your account.'
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })

            send_mail(mail_subject, message, 'midtownsmasher786@gmail.com', [mail])
            return render(request, 'users/email_confirmation.html')
            messages.success(request, 'Success. Now Please Login to continue')
            #return redirect('index')
        else:
            messages.error(request, 'Error. Please Check your form again.')
    else:
        form = StudentCreationForm()
    return render(request, 'users/student-signup.html', {'form': form})


def login(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Login Failed')
            return redirect('index')
    else:
        return render(request, 'home/index.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are logged out')
        return redirect('index')


def edit_faculty_profile(request):
    user_obj = request.user
    if request.method == 'POST':
        form = FacultyCreationForm(
            request.POST, request.FILES, instance=user_obj)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Edited. Login in to continue')
            return redirect('index')
        else:
            messages.error(
                request, 'Error. Please Check your form again.')
    else:
        form = FacultyCreationForm(instance=user_obj)
    return render(request, 'users/edit-profile.html', {'form': form})


def edit_student_profile(request):
    user_obj = request.user
    if request.method == 'POST':
        form = StudentCreationForm(
            request.POST, request.FILES, instance=user_obj)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Edited. Login in to continue')
            return redirect('index')
        else:
            messages.error(
                request, 'Error. Please Check your form again.')
    else:
        form = StudentCreationForm(instance=user_obj)
    return render(request, 'users/edit-profile.html', {'form': form})


def bus_pass(request):
    if request.user.is_authenticated:
        user = request.user
        obj = Pass.objects.all().filter(user=user)
        context = {
            'obj': obj
        }
        return render(request, 'users/bus-pass.html', context)
    else:
        return redirect('index')


def delete_pass(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(Pass, id=id)
        obj.delete()
        messages.success(request, 'Pass Deleted.')
        return redirect('index')
    else:
        return redirect('index')


def print_pass(request, id):
    obj = get_object_or_404(Pass, id=id)
    data = {
        'obj': obj
    }
    return render(request, 'users/pass.html', data)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        print(uid)
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth_login(request, user)
        return redirect('buses')

    else:
        return HttpResponse('Activation link is invalid!')




# Create your views here.


def charge(request):


	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='usd',
			description="Donation"
			)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'users/success.html', {'amount':amount})

def payment(request):
    return render(request,'users/abc.html')
