from django.shortcuts import render
from django.http import HttpResponse
from .models import FilesAdmin

# Create your views here.
def home(request):
    context={'file':FilesAdmin.objects.all()}
    return render(request,'files/home.html',context)

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404