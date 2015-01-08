from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from filer.fields import image


class Project(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255),
    )
    thumbnail = image.FilerImageField()
    sort_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('sort_order',)

    def __unicode__(self):
        return self.safe_translation_getter('title', any_language=True)


class ProjectPicture(TranslatableModel):
    project = models.ForeignKey(Project)
    translations = TranslatedFields(
        description=models.CharField(max_length=255),
    )
    picture = image.FilerImageField()
    sort_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('sort_order',)

    def __unicode__(self):
        return self.safe_translation_getter('description', any_language=True)
