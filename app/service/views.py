from django.shortcuts import render
from django.http.response import JsonResponse

import socket
from datetime import datetime

# Create your views here.


def index(request) -> JsonResponse:
    response = {
        "server": socket.gethostname(),
        "date": str(datetime.now())
    }
    return JsonResponse(data=response, safe=False)
