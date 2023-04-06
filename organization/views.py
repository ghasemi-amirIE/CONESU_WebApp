from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import SurveyForm
from .models import Organization, Survey
from django.http import Http404
from django.views.generic.base import TemplateView
from django.db.models import Avg, Q
from users.models import CustomUser
from django.http import JsonResponse
 

# Create your views here.

def index(request):
    return render(request, 'organization/index.html')
    #template = 'index.html'


class NewOrgView(CreateView):
    model = Organization
    fields = '__all__'
    template_name = 'new_org.html'
    success_url = '/orgs'
 
def success(request):
    return render(request, 'organization/success.html')

def orgs(request):
    #show all orgs
    orgs = Organization.objects.all()
    context = {'organizations': orgs}
    return render(request, "organization/orgs.html", context)

def orgpage(request, org_id):
    org = Organization.objects.get(id = org_id)
    #survey results to put into dashboard
    survey_results = Survey.objects.filter(organization_id = org_id)
    avg_satis = survey_results.aggregate(Avg('satsified'))
    avg_period = survey_results.aggregate(Avg('period'))
    totalsurvs = survey_results.count()
    studs = survey_results.filter(occupation = 'STUD').count()
    emps = survey_results.filter(occupation = 'EMP').count()
    
    context = {'org':org,
               'satisfaction': avg_satis,
               'period':avg_period,
               'count':totalsurvs,
               'studs':studs,
               'emps':emps

               }
    
    return render(request, 'organization/org_page.html', context)


class Pie(TemplateView):
    template_name = 'pie.html'


def survey(request):
    if request.method != 'POST':
        form = SurveyForm()
    else:
        #Post data submitted, process data.
        form = SurveyForm(data = request.POST)
        if form.is_valid():
            new_survey = form.save(commit = False)
            new_survey.participant = request.user
            new_survey.save()
            return redirect('organization:profile')
        
    #Display form.
    context = {'form': form}
    return render(request, 'organization/survey.html', context)


def profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    satis_user = Survey.objects.filter(Q(participant_id=request.user.id)).aggregate(user__satis=Avg('satsified'))
    satis_exc = Survey.objects.filter(~Q(participant_id=request.user.id)).aggregate(avg__satis=Avg('satsified'))             
    context ={
        'f_name':user.first_name,
        'l_name':user.last_name,
        'org':user.organization,
        'position':user.position,
        'satis_exc':satis_exc,
        'satis_user':satis_user
    }
    return render(request, 'organization/profile.html', context)

    



    

