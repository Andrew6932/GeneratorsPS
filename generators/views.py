from django.shortcuts import render

def base(request):
    return render(request, 'base.html')

def msr(request):
    return render(request, 'msr.html')