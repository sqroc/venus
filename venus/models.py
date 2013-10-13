from django.db import models

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=32)

class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    uid =  models.IntegerField()
    name = models.CharField(max_length=30)

class Rss(models.Model):
    rid = models.AutoField(primary_key=True)
    uid =  models.IntegerField()
    cid =  models.IntegerField()
    sitename = models.CharField(max_length=100)
    xmlurl = models.URLField()
    htmlurl = models.URLField()
    updatetime = models.DateField()

class Article(models.Model):
    aid = models.AutoField(primary_key=True)
    rid =  models.IntegerField()
    title = models.CharField(max_length=150)
    pubdate = models.DateField()
    isread =  models.IntegerField()

class Content(models.Model):
    conid =  models.IntegerField(primary_key=True)
    aid =  models.IntegerField()
    description = models.TextField()
    


