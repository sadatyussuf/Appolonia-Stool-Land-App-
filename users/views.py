from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import  render, redirect
# from .forms import NewUserForm
from django.contrib import messages
from .forms import SignUpForm


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "templates/users/user.html")

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('users:login')
    else:
        form = SignUpForm()
    return render(request, 'templates/users/signup.html', {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:            
            return render(request, "templates/users/login.html", {
				"message": "Invalid Credentials"
			})            
    return render(request, "templates/users/user.html")

def logout_view(request):
    logout(request)
    return render(request, "templates/users/login.html", {
		"message": "You are successfully logged out"
	})


def home_view(request):
    return render(request, "templates/property-grid.html")

def property_single(request):
    return render(request, "templates/property-single.html")

def property_grid(request):
    return render(request, "templates/property-grid.html")

def agent_single(request):
    return render(request, "templates/agent-single.html")

def agent_grid(request):
    return render(request, "templates/agents-grid.html")

def blog_single(request):
    return render(request, "templates/blog-single.html")

def blog_grid(request):
    return render(request, "templates/blog-grid.html")

def contact(request):
    return render(request, "templates/contact.html")