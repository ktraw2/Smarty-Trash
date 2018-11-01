from django.shortcuts import render


# Create your views here.
def getdata(request):

    return render(request, "data/getdata.json")
