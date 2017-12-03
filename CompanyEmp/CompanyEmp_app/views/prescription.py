from django.shortcuts import render
from django.http import HttpResponseRedirect
from CompanyEmp_app.views.session import __is_session_open
from CompanyEmp_app.views.user_details import __add_general_content_to_context
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from CompanyEmp_app.models import *

@login_required(login_url='/accounts/login/')
def prescription(request):
    if not __is_session_open(request):
        return HttpResponseRedirect('/')

    user = User.objects.get(username=request.session['user_username'])
    userProfile = UserProfile.objects.get(user=user)

    context = {
        'prescription_page': True
    }

    context.update(__add_general_content_to_context(user,userProfile))


    return render(request, 'prescription.html', context)
