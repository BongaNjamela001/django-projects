from django import forms
from .models import Contact
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Full name',
            'class': 'form-control',
            'style': 'border-color:black; border-radius: 11.33px; width: 100%; height: 45px',
            }))#previous border-color = darkgoldenrod
    email = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Email address',
            'class': 'form-control',
            'style': 'border-color:black; border-radius: 11.33px; width: 100%; height: 45px'
            }))#previous border-color = darkgoldenrod

    brief = forms.CharField(max_length=1000, required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Brief message',
            'style': 'border-color: black; border-radius: 11.33px; width: 100%; height: 120px',
            'rows': 6 #previous border-color = darkgoldenrod
            }))
  
    def get_info(self):
        """
        Returns formatted information
        """
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        user_email = cl_data.get('email')
        message = cl_data.get('brief')

        mail = {
                'name': name,
                'email': user_email,
                'brief': message,
            }
        template = render_to_string('email-template.html', mail)

        return template
    
    #sends email using template format
    def send(self):
        template = self.get_info()
        subject = "Contact Form"
        messag = "New email from portfolio website."
        send_mail(
            subject=subject, 
            message=messag, 
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS],
            html_message=template
        )

    class Meta:
        model = Contact
        fields = ("name", "email", "brief")