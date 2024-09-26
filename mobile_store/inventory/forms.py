from django import forms
from .models import Brand, Phone

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'nationality']

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance')
        super(BrandForm, self).__init__(*args, **kwargs)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if self.instance and self.instance.pk:
            if Brand.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("A brand with this name already exists.")
        else:
            if Brand.objects.filter(name=name).exists():
                raise forms.ValidationError("A brand with this name already exists.")
        return name

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['brand', 'model', 'price', 'color', 'screen_size', 'manufacturer_country', 'quantity']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise forms.ValidationError("Quantity cannot be negative.")
        return quantity

    def clean_screen_size(self):
        screen_size = self.cleaned_data.get('screen_size')
        if screen_size < 0:
            raise forms.ValidationError("Screen size cannot be negative.")
        return screen_size
