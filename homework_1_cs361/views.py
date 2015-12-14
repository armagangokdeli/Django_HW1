
from django.http import HttpResponse
import os



def counting(request,dosya):
    b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    yeni = open("%s/templates/%s"%(b,dosya),'r+')
    a=yeni.read().splitlines()
    yeni.close()
    dictionary={}
    sonuc=''
    for i in range(len(a)):
        if a[i] not in dictionary:
            dictionary[a[i]]=1
        else:
            dictionary[a[i]]+=1

    for k,v in dictionary.items():
        sonuc+='%s:%d<br>'%(k,v)


    return HttpResponse(sonuc)

