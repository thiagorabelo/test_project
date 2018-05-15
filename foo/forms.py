from django import forms


class CoisaForm(forms.Form):
    input_1 = forms.CharField(max_length=255, help_text='Informe os dados aqui', label='Input 1')
    input_2 = forms.CharField(max_length=255, help_text='Informe os dados aqui', label='Input 2')
