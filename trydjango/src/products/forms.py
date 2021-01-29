from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField( widget = forms.TextInput(attrs={"placeholder": "Enter title"}))
    description = forms.CharField(label="desc", required = False, widget = forms.Textarea(
        attrs={
            "class":"textareas",
            "rows": 10,
            "cols": 10,
            "placeholder": "Enter description here"
        }
    ))
    price = forms.DecimalField()

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    

class RawProductForm(forms.Form):
    title = forms.CharField( widget = forms.TextInput(attrs={"placeholder": "Enter title"}))
    description = forms.CharField(label="desc", required = False, widget = forms.Textarea(
        attrs={
            "class":"textareas",
            "rows": 10,
            "cols": 10,
            "placeholder": "Enter description here"
        }
    ))
    price = forms.DecimalField()