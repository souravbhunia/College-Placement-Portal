from django.core import validators
from django import forms
from django.forms import fields, widgets
from .models import User

class StudentProfile(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','id','email','HS_marks','current_cgpa','current_backlogs']
widgets={
    'name':forms.CharField(attrs={'class':'form-control'}),
    'id':forms.IntegerField(attrs={'class':'form-control'}),
    'email':forms.EmailField(attrs={'class':'form-control'}),
    'HS_marks':forms.IntegerField(attrs={'class':'form-control'}),
    'current_cgpa':forms.IntegerField(attrs={'class':'form-control'}),
    'current_backlogs':forms.CharField(attrs={'class':'form-control'}),


}