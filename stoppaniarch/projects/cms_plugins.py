from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models


class ProjectsListingPlugin(CMSPluginBase):
    render_template = 'stoppaniarch/plugins/project_list.html'
    name = _('Projects listing')

    def render(self, context, instance, placeholder):
        context['projects'] = models.Project.objects.all()
        return context

plugin_pool.register_plugin(ProjectsListingPlugin)
