from django.shortcuts import render

# Create your views here.

def jyotshna(request):
    return render(request, 'jyotshna.html')

def harshad(request):
    return render(request, 'harshad.html')
