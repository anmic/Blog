# from django.contrib.auth import logout
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from auth.forms import LoginForm, RegistrationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'],
                                            form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            messages.success(request, "Success register. Let,s login.")
            return HttpResponseRedirec("/tauth/login/")
    else:
        form = RegistrationForm()
    return render_to_response("auth/register.html", {"form": form},
                              context_instance=RequestContext(request))


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None and user.is_active:
                auth.login(request, user)
                messages.success(request, "Welcome, %s.\
                Thanks for logging in." % user.username)
                return HttpResponseRedirect("/articles/all/")
            else:
                messages.error(request, "The username and \
                password were incorrect.")
                return HttpResponseRedirect("/auth/login/")
    else:
        form = LoginForm()
    return render_to_response("auth/login.html", {"form": form},
                              context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    messages.info(request, "You are log out.")
    return HttpResponseRedirect("/auth/login/")
