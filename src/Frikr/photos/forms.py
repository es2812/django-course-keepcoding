from django import forms
from photos.models import Photo
from django.core.exceptions import ValidationError
from photos.settings import BADWORDS

class PhotoForm(forms.ModelForm):
    
    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):
        """
        Validates if description contains badwords defined in settings.BADWORDS
        :return: dict with attr if OK
        """
        cleaned_data = super().clean()

        description = cleaned_data.get("description", "")

        for bw in BADWORDS:
            if bw.lower() in description.lower():
                raise ValidationError("La palabra {0} no está permitida".format(bw))

        return cleaned_data

