from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, '/templates/registration/register.html', {'form': form})

# User profile view
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, '/templates/registration/profile.html', {'form': form})

# User login view (built-in)
from django.contrib.auth.views import LoginView
class CustomLoginView(LoginView):
    template_name = '/templates/registration/login.html'

# User logout view (built-in)
from django.contrib.auth.views import LogoutView
class CustomLogoutView(LogoutView):
    next_page = 'login'
