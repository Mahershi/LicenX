from django.db import models
from django.utils.translation import gettext as _
import datetime


class Project(models.Model):
    identity = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(_("Date"), default=datetime.datetime.now)

    class Meta:
        db_table = "projects"
