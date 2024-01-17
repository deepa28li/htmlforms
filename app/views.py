from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def topicform(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'QLTO':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'topicform.html')


def webpageform(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}

    if request.method=='POST':
        tn=request.POST['tn']
        n=request.POST['n']
        url=request.POST['url']
        mail=request.POST['mail']

        TO=Topic.objects.get(topic_name=tn)
        wo=Webpage.objects.get_or_create(topic_name=TO,name=n,url=url,email=mail)[0]
        wo.save()

        QLWO=Webpage.objects.all()
        d1={'QLWO':QLWO}
        return render(request,'display_webpage.html',d1)
           
    return render(request,'webpageform.html',d)


def accessform(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}

    if request.method=='POST':
       n=request.POST['n']
       d=request.POST['d']
       a=request.POST['a']
       wo=Webpage.objects.get(pk=n)
       ao=Access.objects.get_or_create(name=wo,date=d,author=a)[0]
       ao.save()
       
       QLAO=Access.objects.all()
       d1={'QLAO':QLAO}
       return render(request,'display_accessrecord.html',d1)

    return render(request,'accessform.html',d)

def select_mul_webpage(request):
    
        QLTO=Topic.objects.all()
        d={'QLTO':QLTO}

        if request.method=='POST':
            topiclist=request.POST.getlist('tn')
            # print(tn)
            QLWO=Webpage.objects.none()
            for i in topiclist:
                QLWO=QLWO|Webpage.objects.filter(topic_name=i)
            d1={'QLWO':QLWO}
            return render(request,'display_webpage.html',d1)
        return render(request,'select_mul_webpage.html',d)

def checkbox(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'checkbox.html',d)
 

   



