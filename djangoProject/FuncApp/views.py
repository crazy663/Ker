from django.http import HttpResponse
from django import forms
from django.shortcuts import render
from FuncApp.func import get_content
from FuncApp import func


class UserForm(forms.Form):
    SendMeText = forms.CharField()


def index(request):
    if request.method == 'POST':
        urlpath = request.POST.get('InValue')
        return HttpResponse(f'<h1> Подписки канала: {func.get_content(urlpath)}</h1>')
    else:
        userform = UserForm()
        return render(request, 'index.html', {'form': userform})
