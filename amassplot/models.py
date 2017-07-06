# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# Create your models here.
class GatewayCipres(models.Model):
    TOOL_NAME  = models.TextField(max_length = 100, blank = False, null = False)
    TERMINATE_DATE = models.DateTimeField( primary_key=True )
    ERROR_MSG = models.TextField(max_length = 100, blank = True, null = True)
    RESULT = models.SmallIntegerField(null=True, blank=True)
    REMOTE_JOB_SUBMIT_DATE =  models.DateTimeField( primary_key=True )
    class Meta:
        managed = False
        db_table = 'amass_gateway_cipres'

class CometCipres(models.Model):
    resource_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'comet'

class GordonCipres(models.Model):
    resource_id = models.BigIntegerField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'gordon'




