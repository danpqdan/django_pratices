from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):
    """Formulário para cadastro de usuário, utilizando e-mail como identificador."""

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']  # Certifique-se de que a lista de campos está correta
        labels = {
            'email': 'E-mail',
            'password1': 'Senha',
            'password2': 'Confirmação de Senha',
        }
        widgets = {
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        """Salva o usuário com e-mail como identificador."""
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Define o e-mail como username
        if commit:
            user.save()
        return user

class UsuarioLoginForm(AuthenticationForm):
    """Formulário para login, usando e-mail em vez de username."""

    username = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UsuarioUpdateForm(forms.ModelForm):
    """Formulário para edição dos dados do usuário."""

    class Meta:
        model = User
        fields = ['email']  # Aqui a sintaxe está correta
        labels = {
            'email': 'E-mail',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        """Atualiza o usuário garantindo que username seja o mesmo que o e-mail."""
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user
