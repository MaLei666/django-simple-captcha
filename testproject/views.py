from django.http import HttpResponseRedirect
#from forms import CaptchaForm
from . import forms
from django.shortcuts import render

def home(request):
    if request.POST:
        form = forms.CaptchaForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(request.path + '?ok')
    else:
        form = forms.CaptchaForm()

    return render(request, 'home.html', {'form': form})
