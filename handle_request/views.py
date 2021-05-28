from django.shortcuts import render, HttpResponse
import requests

def home(request):

    url = "http://127.0.0.1:8000/api/uuid_list/"
    result = {

    }

    response = requests.get(url)
    
    for obj in response.json():
        result[obj['timestamp']] = obj['uuid']
    

    # return HttpResponse(f'{response.json()[1]}')
    return HttpResponse(f'{result}')



