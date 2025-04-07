from django import forms
from contact_us.models import ContactUs

class contactUs(forms.Form):
    name = forms.CharField()
    name.widget.attrs.update({'class':'form-control valid','placeholder':'Enter your name'})
    email = forms.CharField()
    email.widget.attrs.update({'class':'form-control valid','placeholder':'Enter your email'})
    subject = forms.CharField()
    subject.widget.attrs.update({'class':'form-control valid','placeholder':'Enter your subject'})
    message = forms.CharField(widget=forms.Textarea())
    message.widget.attrs.update({'class':'form-control valid','placeholder':'Enter your message', 'cols':'30', 'rows':9})