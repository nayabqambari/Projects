from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .form import contactUs
from contact_us.models import ContactUs



def contact_us(request): 

    if request.method == 'POST':
        form = contactUs(request.POST) 
        if form.is_valid():
            n = form.cleaned_data['name']    ## name
            e = form.cleaned_data['email']
            s = form.cleaned_data['subject']
            m = form.cleaned_data['message'] 

            c = ContactUs(name=n, email=e, subject=s, message=m)
            c.save()
            
            form = contactUs()
        return render(request, 'contact_us.html', {'form':form})

    else:
        form = contactUs()
        return render(request, 'contact_us.html', {'form':form})


def contact_post(request): 
    return render(request, 'contact_usa.html')