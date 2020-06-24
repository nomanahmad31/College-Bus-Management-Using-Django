from django.shortcuts import render, redirect
from .models import Contact, Need_Help
from .forms import ContactForm, NeedHelpForm
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        
        
        if form.is_valid():
            contact_obj = form.save(commit=False)
            contact_obj.save()
            mail = form.cleaned_data.get('email')
            send_mail(
            'SRMCEM Bus Management : Contact Enquiry',
            'There has been an enquiry on SRMCEM Bus Management Website. We will contact you soon.',
            'midtownsmasher786@gmail.com',
            [mail],
            fail_silently=False
            )

            send_mail(
            'SRMCEM Bus Management : Contact Enquiry',
            'There has been an enquiry on SRMCEM Bus Management Website. Sign In into the admin panel for more info.',
            'midtownsmasher786@gmail.com',
            ['singhbalkeet@gmail.com'],
            fail_silently=False
            )
            
            messages.success(request, 'Thank You. Your request has been submitted')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {'form': form})


def need_help(request):
    if request.method == 'POST':
        form = NeedHelpForm(request.POST)
        if form.is_valid():
            contact_obj = form.save(commit=False)
            contact_obj.save()
            messages.success(
                request, 'Thanks You. We will try to solve this very soon.')
            return redirect('need-help')
    else:
        form = NeedHelpForm()
    return render(request, "contact/need-help.html", {'form': form})
