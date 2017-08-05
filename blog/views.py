# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse


def index(req):
    t = loader.get_template('index.html')
    c = Context({'uname':'zhuhj'})
    html = t.render(c)
    return HttpResponse(html)
