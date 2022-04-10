from django.shortcuts import render
from landing_page.models import Testimonial
# Create your views here.
def index(request):
    return render(request, 'landing_page/index.html',{
        'testimonials':Testimonial.objects.all()[:10]
    })

def helloWorld(request):
    return render(request, 'landing_page/hello.html',
                  {
                      'django':'Hi My name is IMon','ab':range(10)
                      })