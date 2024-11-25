from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sobre(request):
    html='<html lang="pt-br"><body>Alô mundo</body></html>'
    return HttpResponse(html)