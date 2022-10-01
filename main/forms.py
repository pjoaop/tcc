from turtle import textinput
from django import forms
from .models import *

class QuestaoForm(forms.ModelForm):
    error_css_class = 'error-field' 
    required_css_class = 'forms_style'
    pergunta = forms.CharField(widget=forms.Textarea(attrs={"style":"height : 150px;"}))
    #alternativa1 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    #alternativa2 = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    certa = forms.CharField(widget=forms.TextInput(attrs={"style":"border-color : green;"}))

    class Meta:
        model = Questao
        fields = '__all__'