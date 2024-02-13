from django import forms

class form_mascota(forms.Form):
    nombre = forms.CharField( max_length=15)
    animal = forms.CharField( max_length = 10)

class form_adoptante(forms.Form):
    nombre = forms.CharField(max_length=30)
    mail = forms.EmailField()
    
class form_centro(forms.Form):
    pais = forms.CharField(max_length = 15)
    calle = forms.CharField(max_length = 20)
    abierto = forms.BooleanField()