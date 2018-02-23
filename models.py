# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

BASE_MAX_EXP = 90
# Create your models here.
class Dev(models.Model):
    firstName = models.CharField(max_length=50,null=True,blank=True)
    lastName = models.CharField(max_length=50,null=True,blank=True)
    money = models.IntegerField(null=True,blank=True,default=0)
    fun = models.IntegerField(null=True,blank=True,default=0)
    production = models.IntegerField(null=True,blank=True,default=0)
    exp = models.IntegerField(null=True,blank=True,default=0)
    lv = models.IntegerField(null=True,blank=True,default=0)

    class Meta:
        ordering = ['firstName','lv']

    def __str__(self):
        return self.firstName+WHITE_SPACE+self.lastName

    @property
    def getMaxExp(lv):
        if(lv == 1):
            return BASE_MAX_EXP
        else:
            return getMaxExp(lv-1)*(120/100)
