from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={"class": "new-class-name",
                                             "rows": 20,
                                             "cols": 10}))

    class Meta:
        model = Product
        fields = ["title", "description", "price"]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "MS" in title:
            return title
        else:
            raise forms.ValidationError("This is not a valid title")


class RawProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={"class": "new-class-name",
                                             "rows": 20,
                                             "cols": 10}))
    price = forms.DecimalField()
