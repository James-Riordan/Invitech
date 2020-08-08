from django.shortcuts import render
from .forms import UserRegisterForm
from django.contrib import messages

from django.http import JsonResponse

# Create your views here.

def register(request):
    if(request.method=="POST"):
        #TODO fix me
        form = UserRegisterForm(request.POST)
        print(form.errors.as_data())
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username') # TODO what is this?
            messages.success(request,f'Accunt created for {username}! Login sucker!')
            data = form.cleaned_data
            return JsonResponse(data) 
    else:
        form = UserRegisterForm()
    data = form.errors.as_json()
    return JsonResponse(data, status=400) 

