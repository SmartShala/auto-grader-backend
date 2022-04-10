from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'landing_page/index.html')

def helloWorld(request):
    return render(request, 'landing_page/hello.html',{'django':'Hi My name is IMon','ab':range(10)})