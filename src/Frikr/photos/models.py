from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

PRIVATE = 'PRI'
PUBLIC = 'PUB'

VISIBILITY = {
    (PRIVATE, 'Privada'),
    (PUBLIC, 'Pública')
}
class Photo(models.Model):

    owner = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)

    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)

    def __str__(self):
        return self.name