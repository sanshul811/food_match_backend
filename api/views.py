
from django.shortcuts import render,HttpResponse
from .models import CaffePost  # Import your model
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random
# Create your views here.

@csrf_exempt
def index(request):
    # CaffePost.objects.all().delete()
    if request.method == 'GET':
        data=list(CaffePost.objects.filter().values())
        data_a=list(CaffePost.objects.filter(user='a').values())
        data_b=list(CaffePost.objects.filter(user='b').values())
        arr=[]
        brr=[]
        for i in data_a:
            arr.append(i['name'])

        for i in data_b:
            brr.append(i["name"])   

        crr=[]
        for i in arr:
            if i in brr:
                crr.append(i) 
        print(crr)
        if len(crr)==0:
             response_string = "Hello, waiting for other person to respond"
             return HttpResponse(response_string)
             
        else:
            random_number = random.randint(0, len(crr)-1)
            return JsonResponse(crr[random_number], safe=False)
    else:
        data=json.loads(request.body)
        print(data)
        print("-----------------")
        item=CaffePost(user=data['user'],
        name=data['suit']
        )
        
        item.save()
        # print(data)
        return HttpResponse("Submitted")


