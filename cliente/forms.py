from django import forms

from .models import Cliente



class ClienteModelFrom(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome','cpf','cnpj','endereco','telefone','email']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do cliente'}),
            'cpf': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o CPF do cliente'}),
            'cnpj': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o CNPJ do cliente'}),
            'endereco': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o Endereço do cliente'}),
            'telefone': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o telefone do cliente'}),
            'email': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o email do cliente'}),
        }
