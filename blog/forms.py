from django import forms
from .models import Blog,Hotels,Comments

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
class add_blog(forms.ModelForm):

    class Meta:
        model=Blog
        fields={
            'uploaded_by',
            'discription',
            'location_city',
            'location_state',
            'Country',
            'image',
            'user_discription',

        }
        widgets = {
            'discription': forms.Textarea(attrs={'cols': 80, 'rows': 10 ,'class':'w3-input w3-animate-input' }),

            'user_discription':forms.Textarea(attrs={'cols':80,'rows':2,'class':'w3-input w3-animate-input' }),
            'uploaded_by':forms.Textarea(attrs={'cols':8,'rows':2,'class':'w3-input w3-animate-input' }),
            'location_city':forms.Textarea(attrs={'cols':8,'rows':2,'class':'w3-input w3-animate-input' }),
            'location_state':forms.Textarea(attrs={'cols':80,'rows':2,'class':'w3-input w3-animate-input' }),
            'Country':forms.Textarea(attrs={'cols':80,'rows':2,'class':'w3-input w3-animate-input' }),


            
        }
class comment(forms.ModelForm):
    class Meta:
        model=Comments
        fields={
            'name',
            'comment',
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'w3-input w3-animate-input' }),
            'comment': forms.TextInput(attrs={'class': 'w3-input w3-animate-input'}),
        }