from django import forms
from django.core.validators import FileExtensionValidator
from .models import Venta
from django.utils.safestring import mark_safe

class VentaForm(forms.ModelForm):
    archivos_adjuntos = forms.FileField(
        widget=forms.FileInput(attrs={'multiple': True}),
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'png'])],
        required=False
    )

class MultiFileInput(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        attrs['multiple'] = 'multiple'
        return mark_safe(super().render(name, value, attrs, renderer))

    class Meta:
        model = Venta
        fields = ['cliente', 'producto', 'valor', 'archivos_adjuntos']