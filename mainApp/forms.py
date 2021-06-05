from django import forms

class Formulario(forms.Form):
    fname = forms.CharField(label= 'Primer Nombre')
    lname = forms.CharField(label='Segundo Nombre')
