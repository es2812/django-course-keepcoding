from photos.settings import BADWORDS
from django.core.exceptions import ValidationError

def detect_badwords(value):
    """
    Validates if value contains badwords defined in settings.BADWORDS
    :return: Boolean
    """
    for bw in BADWORDS:
        if bw.lower() in value.lower():
            raise ValidationError("La palabra {0} no está permitida".format(bw))

    return True