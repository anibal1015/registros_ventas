from django import forms
from django.core.validators import FileExtensionValidator
from django.utils.safestring import mark_safe

class MultiFileInput(forms.ClearableFileInput):
    template_name = 'widgets/multi_file_input.html'

    def __init__(self, attrs=None):
        super().__init__(attrs)
        if attrs is None:
            attrs = {}
        attrs['multiple'] = True

    def value_from_datadict(self, data, files, name):
        return files.getlist(name)

    def render(self, name, value, attrs=None, renderer=None):
        attrs['multiple'] = 'multiple'
        return super().render(name, value, attrs, renderer)
