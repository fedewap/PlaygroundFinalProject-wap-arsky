from django.contrib.auth.forms import UserCreationForm, UserModel, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model




class registroform(UserCreationForm):
    username = forms.TextInput()
    email = forms.EmailField(label="email")
    password1 = forms.CharField(label= "Contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label= "Repetir Contraseña", widget = forms.PasswordInput)
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = { k : "" for k in fields }


class UserEditForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Ingrese su email:")
    last_name = forms.CharField(label='Apellido')
    first_name = forms.CharField(label='Nombre')
    imagen = forms.ImageField(label="Avatar", required=False)
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email')
        
        
class form_mascota(forms.Form):
        nombre = forms.CharField(max_length=30)
        animal = forms.CharField(max_length=30)
        fecha_nacimiento = forms.DateField()
        informacion_adicional = forms.CharField(max_length=150, required=False)
        imagen = forms.ImageField(required=False)
