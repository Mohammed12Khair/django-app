from django.shortcuts import render
from django.http.response import JsonResponse

import socket
from datetime import datetime
from .models import TableData

# Create your views here.


def index(request) -> JsonResponse:
    response = {
        "server": socket.gethostname(),
        "date": str(datetime.now())
    }
    return JsonResponse(data=response, safe=False)


def formSave(request):
    if request.method == "POST":
        TableData(name=request.POST['name'],
                  request_details=str(request.headers),
                  server=str(socket.gethostname())).save()

    data = TableData.objects.all().order_by('-id')
    return render(request,
                  'service.html',
                  {"data": data})

    # if request.method == "POST":
    #     name = request.POST['name']
    #     print(request)
