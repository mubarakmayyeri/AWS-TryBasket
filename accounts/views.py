from django.shortcuts import render, redirect
from .models import Account
from .forms import RegistrationForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      email = form.cleaned_data['email']
      phone_number = form.cleaned_data['phone_number']
      password = form.cleaned_data['password']
      
      user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, password=password)
      user.save()
      messages.success(request, 'Registration Successful')
      return redirect('login')
  else:    
    form = RegistrationForm()
  context = {
    'form': form
  }
  
  return render (request, 'accounts/register.html', context)

def login(request):
  if 'email' in request.session:
    return redirect('home')
  
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']
        
    user = auth.authenticate(email=email, password=password)

    if user is not None:
      request.session['email'] = email
      auth.login(request, user)
      # messages.success(request, 'You are now logged in.')
      return redirect('home')
    
    else:
      messages.error(request, 'Invalid credentials')
      return redirect('login')
    
  return render (request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
  if 'email' in request.session:
    request.session.flush()
  auth.logout(request)
  messages.success(request, "You are logged out.")
  return redirect('login')