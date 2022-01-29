from django.shortcuts import render, redirect
from .models import Project, Resume
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home(request):
    return render(request, 'home.html')

def projects(request):
    projects = Project.objects.all()
    context={
        'projects': projects
    }
    return render(request, 'projects.html', context)

def resume(request):
    my_resume = Resume.objects.all()
    context={
        'my_resume': my_resume
    }
    return render(request, 'resume.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            # user_email = str(email.value())
            form.save()
            try:
                send_mail(subject, message, email, [
                          'chepngetichrose2030@gmail.com'], fail_silently=False)
                
                messages.success(request, 'Thanks for contacting me will get back to you as soon as possible')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("home")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


