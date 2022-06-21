from django import forms

class StringForm(forms.Form):
    master_string=forms.CharField(max_length=25)
    string1=forms.CharField(max_length=25)
    string2=forms.CharField(max_length=25)
    string3=forms.CharField(max_length=25)
    string4=forms.CharField(max_length=25)
