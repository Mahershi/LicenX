from django.db import models
from .Project import Project


class Instance(models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT, null=False, blank=False)
    hwid = models.CharField(max_length=50, blank=False, null=False)
    domain = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        db_table = "instances"

    def __str__(self):
        return "[" + str(self.project) + "][" + str(self.domain) + "]"
