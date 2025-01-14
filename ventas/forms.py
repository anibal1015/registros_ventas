from django import forms
from django.core.validators import FileExtensionValidator
from .models import Venta

class MultiFileInput(forms.ClearableFileInput):
    template_name = 'widgets/multi_file_input.html'

    def __init__(self, attrs=None):
        if attrs is None:
            attrs = {}
        attrs['multiple'] = True
        super().__init__(attrs)

    def value_from_datadict(self, data, files, name):
        return files.getlist(name)

    def render(self, name, value, attrs=None, renderer=None):
        attrs['multiple'] = 'multiple'
        return super().render(name, value, attrs, renderer)

class VentaForm(forms.ModelForm):
    archivo_adjunto = forms.FileField(
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx', 'png'])],
        required=False
    )

    class Meta:
        model = Venta
        fields = ['cliente', 'producto', 'valor', 'archivos_adjuntos']
