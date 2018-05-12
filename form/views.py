from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from json import dumps
from django.http import HttpResponseRedirect

@csrf_exempt
def test_form_collection(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    elif request.method == 'POST':
        first_name= request.POST.get('first_name', '')
        print (first_name)
        last_name= request.POST.get('last_name', '')
        email= request.POST.get('email', '')
        print (email)
        password = request.POST.get('password','')
        print (password)
        auth_url  = 'https://secninjaz.herokuapp.com/test_form/'
        payload = {'first_name': first_name, 'last_name': last_name, 'email': email, 'password':password }
        headers = {'content-type':'application/json'}
        r = requests.post(auth_url, headers=headers, data= dumps(payload))
        #return HttpResponseRedirect('http://127.0.0.1:8000/test_form/')
        #return render(request,'login.html')
        return HttpResponseRedirect('http://127.0.0.1:8000/login')

def test_user(request):
    if request.method == 'GET':
        return render(request,'login.html')

    elif request.method == 'POST':
        email= request.POST.get('email', '')
        password = request.POST.get('password','')
        auth_url  = 'https://secninjaz.herokuapp.com/get_details/'
        payload = {'email': email, 'password':password }
        headers = {'content-type':'application/json'}
        r = requests.post(auth_url, headers=headers, data= dumps(payload))
        print (r)
        response_data = r.json()
        try:
            print(response_data[0]['first_name'])
            return HttpResponse(response_data[0]['first_name'] + " successfully logedIn")
        except:
            return HttpResponse("email/password is wrong")
