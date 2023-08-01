from django import forms

from app_catalog.models import Product


BANNED_WORDS = (
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар'
)

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['style'] = 'color: blue;'


    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for banned_word in BANNED_WORDS:
            if banned_word in cleaned_data.lower():
                raise forms.ValidationError(f'Запрещено указывать "{banned_word}" в названии продукта.')
                break
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for banned_word in BANNED_WORDS:
            if banned_word in cleaned_data.lower():
                raise forms.ValidationError(f'Запрещено указывать "{banned_word}" в описании продукта.')
                break
        return cleaned_data
