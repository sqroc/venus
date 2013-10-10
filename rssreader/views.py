from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response,RequestContext
import datetime
import feedparser
import listparser

def current_datetime(request):
     current_date = datetime.datetime.now()
     return render_to_response('current_datetime.html', locals())
 
def upload_file(request):
     UploadFile = request.FILES['file']
     result = listparser.parse(UploadFile.read())
     title = result.meta.title
     return render_to_response('result.html', locals())
     
 
def upload_file2(request):
     return render_to_response('upload.html',context_instance=RequestContext(request))
 
def search_form(request):
    return render_to_response('search_form.html',context_instance=RequestContext(request))

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)