# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import math
BASE_MAX_EXP = 90
WHITE_SPACE = ' '
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

    def getMaxExp(self,lv=1):
        if(lv == 1):
            return BASE_MAX_EXP
        else:
            Mult = 1
            for i in range(lv-1):
                # print('== loop'+str(i)+' ==lv is '+str(lv))
                Mult = round(Mult * 1.2,4)
                # print(Mult)
            return int(round(BASE_MAX_EXP * Mult, 0))