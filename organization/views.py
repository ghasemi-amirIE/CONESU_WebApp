from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import SurveyForm, NewOrgForm
from .models import OrgProfile, Survey
from django.http import Http404
from django.views.generic.base import TemplateView
from django.db.models import Avg, Q, Count
from users.models import CustomUser
from django.http import JsonResponse
 

# Create your views here.

def index(request):
    return render(request, 'organization/index.html')
    #template = 'index.html'


class NewOrgView(CreateView):
    model = OrgProfile
    fields = '__all__'
    template_name = 'new_org.html'
    success_url = '/orgs'
 
def success(request):
    return render(request, 'organization/success.html')

def orgs(request):
    #show all orgs
    orgs = OrgProfile.objects.all()
    context = {'organizations': orgs}
    return render(request, "organization/orgs.html", context)

def orgpage(request, org_id):
    org = OrgProfile.objects.get(id = org_id)
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
    org_count = Survey.objects.filter(participant_id = request.user).values('organization').annotate(count = Count('organization'))                            
    
    passed_orgs = [i['organization'] for i in org_count]
    passed_times = [i['count'] for i in org_count]


    context ={
        'f_name':user.first_name,
        'l_name':user.last_name,
        'org':user.organization,
        'position':user.position,
        'avatar': user.avatar,
        'satis_exc':satis_exc,
        'satis_user':satis_user,
        'passed_orgs': passed_orgs,
        'passed_times':passed_times,
        'org_count': org_count,
    }
    return render(request, 'organization/profile.html', context)

class Landing(TemplateView):
    template_name = "girdtest.html"

    




    
