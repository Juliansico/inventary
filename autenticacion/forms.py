from django import forms
from gestionar_usuarios.models import Usuario
from django.contrib.auth.forms import PasswordResetForm , SetPasswordForm

class FormularioRegistro(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')
    
    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'apellido', 'correo', 'tipo_documento', 'documento', 'telefono', 'rol_de_usuario']
        labels = {
            'username': 'Nombre de usuario',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo electrónico',
            'tipo_documento': 'Tipo de documento',
            'documento': 'Número de documento',
            'telefono': 'Teléfono',
            'rol_de_usuario': 'Rol de usuario',
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit=True):
        usuario = super().save(commit=False)
        password = self.cleaned_data["password1"]
        usuario.set_password(password)
        if commit:
            usuario.save()
        return usuario


# contraseña
class FormularioRecuperarContraseña(PasswordResetForm):
    email = forms.EmailField(label='Correo electrónico')
    
class FormularioNuevaContraseña(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput, label='Nueva contraseña')
    new_password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar nueva contraseña')