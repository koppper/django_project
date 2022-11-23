from django import forms


class StudentForms(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    address = forms.CharField()
    langs = forms.CharField()
