from django.forms import ModelForm
from .models import property

class propertyForm(ModelForm):
    class Meta:
        model = property
        fields = [
            "title",
            "price",
            "num_bedrooms",
            "num_bathrooms",
            "square_footage",
            "address",
            "image"
        ]