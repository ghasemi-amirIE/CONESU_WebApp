from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import SurveyForm
from .models import Organization, Survey
from django.http import Http404
from django.views.generic.base import TemplateView
from django.db.models import Avg
 

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


""" def survey(request):
	context ={}
	form = SurveyForm()
	context = {'form': form}
	if request.GET:
		temp = request.GET
		print(temp)
	return render(request, "survey.html", context) """

""" def survey(request):
    #Add new topic
    if request.method != 'POST':
        form = SurveyForm()
    else:
        #Post data submitted, process data.
        form = SurveyForm(data = request.POST)
        if form.is_valid():
            new_survey = form.save(commit = False)
            new_survey.save()
            return redirect('organization:orgs')
        
    context = {'form': form}
    return render(request, 'organization/survey.html', context) """

class SurveyView(CreateView):
    model = Survey
    fields = '__all__'
    template_name = 'survey.html'
    success_url = '/orgs'


    

