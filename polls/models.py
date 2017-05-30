# coding:utf-8
from django.db import models


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return u'%s' % self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.choice_text

