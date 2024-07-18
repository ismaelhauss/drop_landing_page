from django.shortcuts import render, redirect
from landing.form import MailForm
from .models import Mails

def landing(request):
    if request.method == 'POST':
        form = MailForm(request.POST)
        mails = [mail.mail for  mail in list(Mails.objects.all())]
        if form.is_valid() and request.POST['mail'] not in mails:
            form.save()
            return redirect('/merci')
    else:
        form = MailForm()
    return render(request, 'landing/index.html', {'form' : form})

def mentions(request):
    return render(request, 'landing/mentions.html')

def merci(request):
    return render(request, 'landing/valide.html')