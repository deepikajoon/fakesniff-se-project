from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def landing_page(request):
    return render(request, 'detect/landing.html')
def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not form.cleaned_data['remember_me']:
                    request.session.set_expiry(0)  # Session expires on browser close
                messages.success(request, "Logged in successfully!")
                return redirect('user_dashboard')  # Replace with your dashboard or homepage
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'detect/login.html', {'form': form})

def new_image_save(request):
    return render(request, 'detect/new_image_save.html')
def report_sent_success(request):
    return render(request, 'detect/report_sent_sucess.html')
def feedback_page(request):
    return render(request, 'detect/feedback.html')
def user_dashboard(request):
    return render(request, 'detect/user_dashboard.html')
def admin_dashboard(request):
    return render(request, 'detect/admin_dashboard.html')
def result(request):
    confidence = 85
    return render(request, 'detect/result.html', {'confidence': confidence})
def chatbot_page(request):
    return render(request, 'detect/chatbot_page.html')

def signup_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Auto-login after signup
            messages.success(request, "Account created successfully!")
            return redirect('user_dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SignupForm()
    return render(request, 'detect/signup.html', {'form': form})

