from django.http import HttpResponse
from django.template import loader
from .models import Relative

def relatives(request):

    relatives = Relative.objects.all()
    template = loader.get_template('relatives.html')
    context = {'relatives': relatives}
    render = template.render(context)  
    return HttpResponse(render)

