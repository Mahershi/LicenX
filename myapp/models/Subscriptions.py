from django.db import models
from .Instance import Instance
from django.utils.translation import gettext as _
import datetime


class Subscriptions(models.Model):
    instance = models.ForeignKey(Instance, on_delete=models.PROTECT, default=False, null=False)
    # default expires on the day it was created
    expires = models.DateTimeField(_("Expires"), default=datetime.datetime.now)
    last_checkin = models.DateTimeField(null=True)
    bypass = models.BooleanField(default=False)
    # 7 days grace period
    grace_period = models.IntegerField(default=7)
    checkin_interval = models.IntegerField(default=86400)

    class Meta:
        db_table = "subscriptions"

    def __str__(self):
        return str(self.instance) + "[" + str(self.expires) + "]"
