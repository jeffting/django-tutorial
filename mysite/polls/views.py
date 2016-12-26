from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
        return HttpResponse("Hello, world. You' deserve a punch in my nuts.")

# Create your views here.

class ButtView(TemplateView):
    template_name = 'butt.html'
