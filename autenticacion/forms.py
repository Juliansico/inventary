from django import forms
from gestionar_usuarios.models import Usuario

class FormularioRegistro(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')
    
    class Meta:
        model = Usuario
        fields = ['usuario', 'nombre', 'apellido', 'correo', 'tipo_documento', 'documento', 'telefono', 'rol_de_usuario']
        labels = {
            'usuario': 'Nombre de usuario',
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

    def clean_usuario(self):
        usuario = self.cleaned_data.get('usuario')
        if not usuario:
            raise forms.ValidationError("El nombre de usuario no puede estar vacío.")
        return usuario

    def save(self, commit=True):
        usuario = super().save(commit=False)
        password = self.cleaned_data["password1"]
        usuario.set_password(password)
        if commit:
            usuario.save()
        return usuario




# contraseña
class RecuperarContrasenaForm(forms.Form):
    email = forms.EmailField()

class RestablecerContrasenaForm(forms.Form):
    nueva_contrasena = forms.CharField(widget=forms.PasswordInput())
    confirmacion_contrasena = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super().clean()
        nueva_contrasena = cleaned_data.get('nueva_contrasena')
        confirmacion_contrasena = cleaned_data.get('confirmacion_contrasena')

        if nueva_contrasena and confirmacion_contrasena and nueva_contrasena != confirmacion_contrasena:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return cleaned_data