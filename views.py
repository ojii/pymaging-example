import sys
from django import forms
import django
from django.http import HttpResponse
import base64
from django.shortcuts import render_to_response
from django.template import RequestContext
from pymaging import Image

FAVICON = (
    b'AAABAAEAEBACAAEAAQCwAAAAFgAAACgAAAAQAAAAIAAAAAEAAQAAAAAAAAAAAAAAAAAAAAAA'
    b'AAAAAAAAAAD///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
)


class PymagingForm(forms.Form):
    image = forms.ImageField()

def index(request):
    if request.method == 'POST':
        form = PymagingForm(request.POST, request.FILES)
    else:
        form = PymagingForm()
    if form.is_valid():
        response = HttpResponse(content_type='image/png')
        image = Image.open(form.cleaned_data['image'])
        image = image.resize(200, 200)
        image.save(response, 'png')
        return response
    context = RequestContext(request)
    context['form'] = form
    context['python'] = sys.version
    context['django'] = django.get_version()
    return render_to_response('index.html', context)

def favicon(request):
    return HttpResponse(base64.b64decode(FAVICON), content_type='image/x-icon')
