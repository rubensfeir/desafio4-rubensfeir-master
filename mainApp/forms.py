from django import forms

class Formulario(forms.Form):
    user = forms.IntegerField()
    fname = forms.CharField(label= 'Primer Nombre')
    lname = forms.CharField(label='Segundo Nombre')

    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label = 'Contraseña', max_length=32, widget=forms.PasswordInput)

class IniciarSesion(forms.Form):
    username = forms.CharField(label= 'Nombre de Usuario')
    password = forms.CharField(label= 'Contraseña', max_length=32, widget=forms.PasswordInput)

class Proyecto(forms.Form):
    nombre= forms.CharField(label='nombre del proyecto')
    descripcion = forms.CharField(label='descripcion del proyecto')