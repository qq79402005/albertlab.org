import os
import sys
from django.conf import settings

# django settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

from django import forms
from django.conf.urls import url
from django.http import HttpResponse

from io import BytesIO
from PIL import Image, ImageDraw

class ImageForm(forms.Form):
    height = forms.IntegerField(min_value=1, max_value=2048)
    width = forms.IntegerField(min_value=1, max_value=2048)

    def generate(self, image_format='PNG'):
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        image = Image.new('RGB', (width, height))
        draw = ImageDraw.Draw(image)
        text = '{} X {}'.format(width, height)
        textwidth, textheight = draw.textsize(text)
        if(textwidth<width and textheight<height):
            draw.text((0, 0), text, fill=(255,255,255))
        content = BytesIO()
        image.save(content, image_format)
        content.seek(0)
        return content

def placeholder(request, width, height):
    # TODO Rest of the view will go here
    form = ImageForm({'height':height, 'width':width})
    if form.is_valid():
        image = form.generate()

        return HttpResponse(image, content_type='image/png')
    else :
        return HttpResponseBadRequest('Invalid Image Request')

def index(request):
    return HttpResponse('Hello World')

# url pattern fot the server root.
urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
    url(r'^$', index, name='homepage'),
)

# WSGI
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Management
if __name__ == '__main__' :
    from django.core.management import execute_from_command_line
    
    execute_from_command_line( sys.argv)