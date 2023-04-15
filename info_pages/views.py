from django.shortcuts import render

# Create your views here.

def project(request, project_name):
    return render(request, 'static/project.html', {'project_name': project_name})