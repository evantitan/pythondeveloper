from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm
import logging
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class SignupView(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm

    def get_success_url(self):
        redirect_to = self.request.GET.get('next', '/')
        return redirect_to

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save()
        email = form.cleaned_data.get('email')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=raw_password)
        login(self.request, user)
        messages.info(self.request, "you have signed up successfully.")
        return response
