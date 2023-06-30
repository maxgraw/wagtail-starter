from django.db import models

from wagtail.documents.models import AbstractDocument
from wagtail.images.models import AbstractImage, AbstractRendition
from wagtailmedia.models import AbstractMedia

class CustomStarterImage(AbstractImage):
    pass


class CustomStarterRendition(AbstractRendition):
    image = models.ForeignKey(
        "CustomStarterImage", on_delete=models.CASCADE, related_name="renditions"
    )

    class Meta:
        unique_together = (("image", "filter_spec", "focal_point_key"),)


class CustomStarterDocument(AbstractDocument):
    pass


class CustomStarterMedia(AbstractMedia):
    pass
