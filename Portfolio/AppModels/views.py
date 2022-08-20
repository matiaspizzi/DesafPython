from django.http import HttpResponse
from django.template import loader
from .models import Relative

def home(request):
    relatives = Relative.objects.all()
    template = loader.get_template('AppModels/home.html')
    return HttpResponse(template.render({'relatives': relatives}))