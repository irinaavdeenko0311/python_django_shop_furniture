from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ImagesForm(forms.Form):
    """
    Форма для загрузки нескольких изображений.

    Используется в административной панели.
    """
    file_field = MultipleFileField()


class CSVForm(forms.Form):
    """
    Форма для загрузки файла CSV.

    Используется в административной панели.
    """
    csv_file = forms.FileField()
