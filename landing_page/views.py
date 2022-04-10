from django.shortcuts import redirect, render
from landing_page.models import Testimonial,QueryData
# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'landing_page/index.html',{
            'testimonials':Testimonial.objects.all()[:10]
        })
    elif request.method =='POST':
        institute_name = request.POST.get('inst_name')
        if institute_name == '': institute_name = None
        email = request.POST.get('email')
        if email == '': email = None
        ph_no = request.POST.get('phone_number')
        if ph_no == '': ph_no = None
        message = request.POST.get('message')
        if message == '': message = None
        if all([institute_name,email,message]):
            QueryData.objects.create(
                name = institute_name,
                email = email,
                ph_no = ph_no,
                message = message,
            )
        return redirect('landing:index')

def helloWorld(request):
    return render(request, 'landing_page/hello.html',
                  {
                      'django':'Hi My name is IMon','ab':range(10)
                      })
    
    