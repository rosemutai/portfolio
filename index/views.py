from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request, 'home.html')

def contactView(request):
    return render(request, 'home.html')