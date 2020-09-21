from django.shortcuts import render
from django.views import View

# Create your views here.

class Login(View):
    def get(self,request):
        error_info = request.session.pop("error_info", "")
        return render(request, 'login.html', context={"error_info": error_info})



def index(request):
    return render(request, 'index.html')

def upload(request):
    return render(request, 'upload.html')

