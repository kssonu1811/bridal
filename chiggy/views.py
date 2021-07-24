from bridal_function.models import bridal
from django.shortcuts import render, redirect
from bridal_function.models import bridal
from . models import Team
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    feature_bridal = bridal.objects.order_by('created_date')
    teams = Team.objects.all()
    all_bridal = bridal.objects.order_by('created_date')
    sub_title_search = bridal.objects.values_list('sub_title', flat=True).distinct()
    type_search = bridal.objects.values_list('type', flat=True).distinct()
    design_search = bridal.objects.values_list('design', flat=True).distinct()
    purpose_search = bridal.objects.values_list('purpose', flat=True).distinct()
    aouther_name_search = bridal.objects.values_list('aouther_name', flat=True).distinct()
    service_place_search = bridal.objects.values_list('service_place', flat=True).distinct()
    data = {
        'feature_bridal': feature_bridal,
        'teams' : teams,
        "all_bridal" : all_bridal,
        "sub_title_search" : sub_title_search,
        "type_search" : type_search,
        "design_search" : design_search,
        "purpose_search" : purpose_search,
        "aouther_name_search" : aouther_name_search,
        "service_place_search" : service_place_search,
    }
    return render(request, 'chiggy/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request,'chiggy/about.html',data)

def services(request):
    return render(request,'chiggy/service.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']
        
        email_subject = 'you have new message from Carzone website regarding' +subject
        messages_body ='Name:' +name+ 'Email' +email+ 'subject' +subject+ 'phone' +phone+ 'messages' +message

        admin_info = User.objects.get(is_superuser = True)
        admin_email = admin_info.email

        send_mail(
            email_subject,
            messages_body,
            'ksajansonu@gmail.com',
            [admin_email],
            fail_silently=False,
        )
    
        messages.success(request,'Thankyou for contacting us. We will get back to you shortly')
        return redirect('contact')
    return render(request,'chiggy/contact.html')


def search(request):
    bridals = bridal.objects.order_by('created_date')
    sub_title_search = bridal.objects.values_list('sub_title', flat=True).distinct()
    type_search = bridal.objects.values_list('type', flat=True).distinct()
    design_search = bridal.objects.values_list('design', flat=True).distinct()
    purpose_search = bridal.objects.values_list('purpose', flat=True).distinct()
    aouther_name_search = bridal.objects.values_list('aouther_name', flat=True).distinct()
    service_place_search = bridal.objects.values_list('service_place', flat=True).distinct()
    
    
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            bridals = bridals.filter(type__icontains=keyword)

    if 'sub_title' in request.GET:
        sub_title = request.GET['sub_title']
        if sub_title:
            bridals = bridals.filter(sub_title__iexact=sub_title)

    if 'type' in request.GET:
        type = request.GET['type']
        if type:
            bridals = bridals.filter(type__iexact=type)


    if 'design' in request.GET:
        design = request.GET['design']
        if design:
            bridals = bridals.filter(design__iexact=design)

    if 'purpose' in request.GET:
        purpose = request.GET['purpose']
        if purpose:
            bridals = bridals.filter(purpose__iexact=purpose)

    if 'aouther_name' in request.GET:
        aouther_name = request.GET['aouther_name']
        if aouther_name:
            bridals = bridals.filter(aouther_name__iexact=aouther_name)
    if 'service_place' in request.GET:
        service_place = request.GET['service_place']
        if service_place:
            bridals = bridals.filter(service_place__iexact=service_place)


    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            bridals = bridals.filter(cost__gte=min_price, cost__lte=max_price)
    
    data ={
        'bridals' : bridals,
        "service_place_search" : service_place_search,
        "aouther_name_search" : aouther_name_search,
        "purpose_search" : purpose_search,
        "design_search" : design_search,
        "sub_title_search" : sub_title_search,
        "type_search" : type_search
        
    }
    return render(request, 'chiggy/search.html',data)
 