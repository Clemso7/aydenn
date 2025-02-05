from django.shortcuts import render
from .models import Emploi
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    jobs = Emploi.objects.all().order_by('-id').filter(close=False)
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get("page")
    jobs = paginator.get_page(page_number)
    context ={'jobs':jobs}
    return render(request, 'pages/index.html', context)

# Faq view
def mission(request):
    return render(request, 'pages/mission.html')
# Contact view
def contact(request):
    return render(request, 'pages/contact.html')

# policy of confidentiality view
def confidentialite(request):
    return render(request, 'pages/confidentialite.html')

#job view
def jobs(request):
    jobs = Emploi.objects.all().order_by('-id').filter(close=False)
    paginator = Paginator(jobs, 10)
    page_number = request.GET.get("page")
    jobs = paginator.get_page(page_number)
    context ={'jobs':jobs}
    return render(request, "pages/jobs.html", context)

#job-detail view
def jobs_details(request, id):
    job = Emploi.objects.get(pk=id)
    context ={'job':job}
    return render(request, "pages/jobs-details.html", context)