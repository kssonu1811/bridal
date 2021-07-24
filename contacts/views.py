from django.contrib.auth.models import User
from contacts.models import Contact
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from bridal_function.models import bridal
# Create your views here.


def inquiry(request):
    if request.method =='POST':
        bridal_id = request.POST['bridal_id']
        bridal_title = request.POST['bridal_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone_number =request.POST['phone_number']
        fax_number = request.POST['fax_number']
        messagees = request.POST['messagees']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted =Contact.objects.all().filter(bridal_id=bridal_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'you have already made an inquiry about this Bridal function. Please wait untill we get back to you.')
                return redirect('bridal:bridal_detail', bridal_id)

        contact = Contact(bridal_id=bridal_id, bridal_title=bridal_title, user_id=user_id, first_name=first_name, last_name=last_name, customer_need=customer_need, city=city, state=state, email=email, phone_number=phone_number, fax_number=fax_number, messagees=messagees)
        
        admin_info = User.objects.get(is_superuser = True)
        admin_email = admin_info.email
        send_mail(
            'New bridal Inquiry',
            'You have a new inquiry message for ' +bridal_title+ '. Please login to admin panel for more information',
            'ksajansonu@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request,'Thankyou, Your request has been submitted . We will get back to you shortly')
        return redirect('bridal:bridal_detail', bridal_id)

