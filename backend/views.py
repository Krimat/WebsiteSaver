import os
from django.http import HttpResponse
from django.conf import settings


def index(reques):
    with open(os.path.join(settings.REACT_ROOT, 'index.html')) as fout:
        return HttpResponse(fout.read())