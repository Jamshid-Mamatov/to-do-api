from django.shortcuts import render

from django.http import HttpResponse
import json

information={'mission':[]}

def home(request):
    task=request.GET.get("task")
    print(task)
    missions=""
    if task!=None:
        information["mission"].append(task)
        with open("database.json",'w') as f:
            json.dump(information,f)

        with open('database.json','r') as f:
            data=json.load(f)
            print(data['mission'])
            
            for i  in data['mission']:
                missions+=i
                missions+="<br>"

    return HttpResponse(missions)
    

def removeTask(request):

    task=request.GET.get("task")
    print(task)
    missions=""
    if task==None:
        

        with open('database.json','r') as f:
            data=json.load(f)
            print(data['mission'])
            
            for i  in data['mission']:
                missions+=i
                missions+="<br>"

        return HttpResponse(missions)
    else:
        with open('database.json', 'r') as f:
            data=json.load(f)
        
            data['mission'].remove(task)
            print(data['mission'])
            for i  in data['mission']:
                missions+=i
                missions+="<br>"
 
        
            with open('database.json', 'w') as f:
                json.dump(data, f)
        
 
        return HttpResponse(missions)
        

   

