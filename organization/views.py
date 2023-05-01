from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import SurveyForm, ContactForm
from .models import OrgProfile, Survey
from django.db.models import Avg, Q, Count, F
from users.models import CustomUser
 

# Create your views here.

def index(request):
    if request.method != 'POST':
        form = ContactForm()
    else:
        #Post data submitted, process data.
        form = ContactForm(data = request.POST)
        if form.is_valid():
            new_survey = form.save(commit = False)
            new_survey.participant = request.user
            new_survey.save()
            return redirect('organization:index')
        
    #Display form.
    context = {'form': form}
    return render(request, 'organization/index.html', context)


class NewOrgView(CreateView):
    model = OrgProfile
    fields = '__all__'
    template_name = 'new_org.html'
    success_url = '/users/register'


def orgpage(request, org_id):
    org = OrgProfile.objects.get(id = org_id)

    #survey results to put into dashboard
    survey_results = Survey.objects.filter(organization_id = org_id)

    satis_stud = survey_results.filter(occupation = "STUD").aggregate(Avg('satsified'))
    satis_emp = survey_results.filter(occupation = "EMP").aggregate(Avg('satsified'))
    avg_period = survey_results.aggregate(Avg('period'))
    totalsurvs = survey_results.count()
    studs = survey_results.filter(occupation = 'STUD').count() 
    emps = survey_results.filter(occupation = 'EMP').count()

    #Radar chart queries
    stud_data = survey_results.filter(occupation='STUD').aggregate(
    avg_period=Avg('period'),
    avg_satisfaction=Avg('satsified'),
    response_count=Count('occupation'))

    emp_data = survey_results.filter(occupation='EMP').aggregate(
    avg_period=Avg('period'),
    avg_satisfaction=Avg('satsified'),
    response_count=Count('occupation'))
    
    context = {'org':org,
               'satis_stud':satis_stud,
               'satis_emp': satis_emp,
               'period':avg_period,
               'count':totalsurvs,
               'studs':studs,
               'emps':emps,
               'stud_projects': list(stud_data.values()),
               'emp_projects': list(emp_data.values()),
               }
    
    return render(request, 'organization/org_page.html', context)


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
    user = CustomUser.objects.get(id=request.user.id) #Returns user info

    survey = Survey.objects.all()#Returns all survey data

    survey_satisfaction = survey.aggregate(
    user_satisfaction=Avg('satsified', filter=Q(participant_id=request.user.id)),
    avg_satisfaction=Avg('satsified', filter=~Q(participant_id=request.user.id))
    )

    org_count = survey.filter(participant_id = request.user.id).values('organization').annotate(count = Count('organization'))   
    #instead of the list with values separated by comma, for loop in profile html gives unseparated numbers
    #easier to send the data in right format directly to html
    passed_orgs = [i['organization'] for i in org_count]
    passed_times = [i['count'] for i in org_count]

    all_surv = survey.filter(participant_id=request.user.id).values()    
    #for loop for chart.js
    org_label = [i['organization_id'] for i in all_surv]              
    surv_data = [i['satsified'] for i in all_surv]              
    

    context ={
        'user':user,
        'surv_satis': survey_satisfaction,
        'passed_orgs': passed_orgs,
        'passed_times':passed_times,
        'org_label':org_label,
        'surv_data':surv_data,
        'org_count': org_count,
    }

    
    return render(request, 'organization/profile.html', context)








    
