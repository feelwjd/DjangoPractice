from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
count = 0

def index(request):
    return render(request, 'index.html')

@csrf_exempt

def result(request):
    global count
    count = count + 1
    name=request.POST['name']
    pw=request.POST['pw']
    return render(request, 'result.html',{'name': name, 'pw':pw, 'cnt':count})
