from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from .models import CustomUser

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("organization:index")
    template_name = "registration/registration.html"

def edit_profile(request):
    user = CustomUser.objects.get(pk=id)
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST, instance=request.user)
        
        if user_form.is_valid():
            user_form.save()
            return render('organizations/profile.html')
    else:
        user_form = CustomUserCreationForm(instance=request.user)

    context = {'user_form': user_form}
    return render(request, 'edit_profile.html', context)

def edit_profile(request):
    args = {}

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return render(reverse('profile'))
    else:
        form = CustomUserCreationForm()

    args['form'] = form
    return render(request, 'user_profiles/edit_profile.html', args)
