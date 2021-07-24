from django.shortcuts import render,get_object_or_404
from bridal_function.models import bridal as bridals
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def bridal(request):
    
    feature_bridal = bridals.objects.order_by('created_date')
    paginator = Paginator(feature_bridal, 4)
    page = request.GET.get('page')
    paged_bridal = paginator.get_page(page)
    data ={
        'feature_bridal' : paged_bridal,
    }
    return render(request,'bridal/bridal.html', data)

def bridal_detail(request, id):
    single_bridal = get_object_or_404(bridals, pk=id)
    data = {
        'single_bridal': single_bridal,
    }
    return render(request, 'bridal/bridal_details.html',data)