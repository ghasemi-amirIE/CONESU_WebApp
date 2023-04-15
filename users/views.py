from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationForm
from .models import CustomUser

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("organization:index")
    template_name = "registration/registration.html"

def update_user_profile(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)
            return redirect(reverse('organization:profile'))  # Redirect and Reverse to the profile page
    else:
        form = CustomUserCreationForm(instance=request.user)

    return render(request, 'user_profiles/edit_profile.html', {'form': form})
