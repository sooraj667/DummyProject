from django.shortcuts import render
from . models import *

def base(request):

    riders=Rider.objects.all()
    context={"riders":riders}
    return render(request,"base.html",context)