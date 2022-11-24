from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Full name',
            'class': 'form-control',
            'style': 'border-color:darkgoldenrod; border-radius: 11.33px; width: 1182px; height: 45px',
            }))
    email = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Email address',
            'class': 'form-control',
            'style': 'border-color:darkgoldenrod; border-radius: 11.33px; width: 1182px; height: 45px'
            }))

    brief = forms.CharField(max_length=1000, required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Brief message',
            'style': 'border-color:darkgoldenrod; border-radius: 11.33px; width: 1182px; height: 120px',
            'rows': 6
            }))

    class Meta:
        model = Contact
        fields = ("name", "email", "brief")