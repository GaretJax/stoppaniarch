from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable.admin import SortableAdminMixin, SortableInlineAdminMixin

from parler.admin import TranslatableAdmin, TranslatableTabularInline

from . import models


class ProjectPictureInline(SortableInlineAdminMixin,
                           TranslatableTabularInline,
                           admin.TabularInline):
    model = models.ProjectPicture

admin.site.register(models.ProjectPicture, TranslatableAdmin)


class ProjectAdmin(SortableAdminMixin,
                   TranslatableAdmin,
                   admin.ModelAdmin):
    enable_sorting = True
    list_display = ['image_thumb', 'title', 'language_column']

    def image_thumb(self, obj):
        if obj.thumbnail:
            return mark_safe(u'<img src="{}" width="32" height="32" />'.format(
                obj.thumbnail.icons['32']))

    image_thumb.short_description = 'Thumbnail'
    image_thumb.allow_tags = True

    @property
    def media(self):
        return super(ProjectAdmin, self).media

    inlines = [
        ProjectPictureInline,
    ]

admin.site.register(models.Project, ProjectAdmin)
