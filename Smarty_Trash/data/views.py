from django.shortcuts import render


# Create your views here.
def livedata(request):
    return render(request, "data/livedata.json")

def statistics(request):
    return render(request, "")
