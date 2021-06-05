from django import forms

class Formulario(forms.Form):
    user = forms.IntegerField()
    fname = forms.CharField(label= 'Primer Nombre')
    lname = forms.CharField(label='Segundo Nombre')

    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label = 'Contraseña', max_length=32, widget=forms.PasswordInput)



