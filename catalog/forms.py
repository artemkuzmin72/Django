from django import forms
from .models import Product
from django.core.validators import MinValueValidator

class ProductForm(forms.ModelForm):
    forbidden_words = [
        "казино", "криптовалюта", "крипта",
        "биржа", "дешево", "бесплатно", "обман",
        "полиция", "радар"
    ]

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'pics', 'category']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите имя'  # Текст подсказки внутри поля
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание'  # Текст подсказки внутри поля
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите цену'  # Текст подсказки внутри поля
        })

    def clean_name(self):
        name = self.cleaned_data['name']
        for word in self.forbidden_words:
            if word.lower() in name.lower():
                raise forms.ValidationError(f"Слово '{word}' нельзя использовать в названии.")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for word in self.forbidden_words:
            if word.lower() in description.lower():
                raise forms.ValidationError(f"Слово '{word}' нельзя использовать в описании.")
        return description
    
    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise forms.ValidationError("Цена продукта не может быть отрицательной.")
        return price