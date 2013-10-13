from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext
from venus.models import User, Category, Rss
import urllib2
import datetime
import feedparser
import listparser


def upload_opml(request):
     return render_to_response('uploadopml.html', context_instance=RequestContext(request))

def upload_opml_file(request):
     UploadFile = request.FILES['file']
     result = listparser.parse(UploadFile.read())
     title = result.meta.title
     if title != '' :
         count = 0;
         for i in result.feeds:
             c1 = Category(uid=1, name=i.tags)
             c2 = Category.objects.filter(name=i.tags)
             if c2.count() == 0:
                 c1.save()
             else: 
                 c1.cid = c2[0].cid
             r1 = Rss(uid=1, cid=c1.cid, sitename=i.title, xmlurl=i.url, htmlurl='', updatetime=datetime.datetime.now())
             r1.save()
             count += 1
        
     return render_to_response('resultopml.html', locals())
     
def get_rss(request):
    myrss = Rss.objects.filter(uid=1)
    urllib2.urlopen( 'http://www.dbanotes.net/atom.xml' ).read()
    #d = feedparser.parse('http://www.dbanotes.net/atom.xml')
    #title = d['feed']['title']
    title = 'ddd'
    return render_to_response('resultopml.html', locals())
