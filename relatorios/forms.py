from django import forms


class RelatorioVendaForm(forms.Form):
    data_inicio = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    data_fim = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
