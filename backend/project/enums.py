from django.db import models
from django.utils.translation import ugettext as _


class ProjectState(models.TextChoices):
    WORKING = 'WORKING', _('Working')
    HALT = "HALT", _("Halt")
    DONE = "DONE", _("Done")


class TaskState(models.TextChoices):
    WORKING = 'WORKING', _('Working')
    HALT = "HALT", _("Halt")
    DONE = "DONE", _("Done")
    UNASSIGNED = "UNASSIGNED", _("Unassigned")
    TODO = "TODO", _("Todo")
