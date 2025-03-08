from django.db import models
from .User import User
from django.utils.translation import gettext as _
import datetime


class Project(models.Model):
    identity = models.CharField(max_length=20, null=False, blank=False)
    created_at = models.DateTimeField(_("Created At"), default=datetime.datetime.now)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)

    class Meta:
        db_table = "projects"

    def __str__(self):
        return str(self.identity)
