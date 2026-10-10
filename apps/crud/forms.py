from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome','cpf','email','telefone','data_nascimento','sintomas']
        widgets = {
            'nome':forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':"nome",
                    'required':True,
                },
            ),
            'cpf':forms.TextInput(
                attrs={
                    'class':"form-control",
                    'id':"cpf",
                    'required':True,
                },
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':"form-control",
                    'id':"email",
                    'required':True,
                },
            ),
            'telefone':forms.TelInput(
                attrs={
                    'class':"form-control",
                    'id':"telefone",
                    'required':True,
                },
            ),
            'data_nascimento':forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type':"date",
                    'class':"form-control",
                    'id':"data_nascimento",
                    'required':True,
                },
            ),
            'sintomas':forms.Textarea(
                attrs={
                    'id':"sintomas",
                    'rows':3,
                    'class': 'form-control'
                },
            ),
        }
        error_messages = {
            'email':{
                'unique': "E-mail já cadastrado.",
            },
            'cpf':{
                'unique': "CPF já cadastrado.",
            },
        }