from django import forms
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
    form = PymagingForm(request.POST, request.FILES)
    if form.is_valid():
        response = HttpResponse(content_type='image/png')
        image = Image.open(form.cleaned_data['image'])
        image = image.resize(200, 200)
        image.save(response, 'png')
        return response
    return render_to_response('index.html', RequestContext(request, {'form': form}))

def favicon(request):
    return HttpResponse(base64.b64decode(FAVICON), content_type='image/x-icon')

