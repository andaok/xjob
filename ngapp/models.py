# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ng(models.Model):
    ng_name = models.CharField(max_length=50,unique=True)
    vip = models.CharField(max_length=50,unique=True)
    nodes_ip = models.CharField(max_length=128)
    comment = models.TextField(null=True,blank=True)

    def __unicode__(self):
        return self.ng_name


class upstream(models.Model):
    ng = models.ForeignKey(ng)
    consul_service_name = models.CharField(max_length=64)
    service_site_name = models.CharField(max_length=64)
    plan_service_nodes = models.TextField()

    class Meta:
        unique_together = ("ng","service_site_name")

    def __unicode__(self):
        return self.service_site_name




