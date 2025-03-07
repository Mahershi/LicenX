from django.db import models
from .Project import Project
from .User import User


class Instance(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    hwid = models.CharField(max_length=50, blank=False, null=False)
    domain = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        db_table = "instances"
