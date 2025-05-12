from django import forms
from .models import HabilidadeUsuario

class FormularioHabilidade(forms.ModelForm):
    class Meta:
        model = HabilidadeUsuario
        fields = ['habilidade', 'nivel']  # Changed from 'habilidades' to 'habilidade'
        widgets = {
            'habilidade': forms.Select(attrs={'class': 'form-select'}),  # Changed from 'habilidades' to 'habilidade'
            'nivel': forms.Select(attrs={'class': 'form-select'}),
        }
