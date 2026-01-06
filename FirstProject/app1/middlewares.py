import json 
from django.http import HttpResponse,JsonResponse

# class Middleware:
#     def __init__(self,get_response):
#         print("server starrted by harish")
#         self.get_response=get_response

#     def __call__(self,request):
#         print(request.path)  
#         if request.path=="/second/":
#             print("middleware started working")      
#         response=self.get_response(request)
#         return response


# class Middleware1:
#     def __init__(self,get_response):
#         print("server starrted by harish-mw1")
#         self.get_response=get_response

#     def __call__(self,request): 
#         print(request.path) 
#         if request.path=="/getStudents/" and request.method=="GET":
#             print("middleware started working-mw1")      
#         response=self.get_response(request)
#         return response


# __init__--->ready to get response 

# __call__-->ready to send the response as per user request.

class SSCMiddleware():
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if request.path=="/job1/":            
            incoming_data=json.loads(request.body)            
            ssc_status=incoming_data.get("ssc_status")
            if ssc_status == "True":
                response=self.get_response(request) 
                print(response,"hellooooo")
                return response 
            return JsonResponse({"status":"failure","msg":"u should qualify ssc to apply for this job"})     

class MedicalFitMiddleWare():
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print(request.method,"job2 mf")
        if request.path =="/job2/": 
            print("mf triggered")          
            incoming_data=json.loads(request.body)            
            medically_fit=incoming_data.get("medically_fit")
            if medically_fit == "True":
                response=self.get_response(request) 
                print(response,"hellooooo")
                return response 
            return JsonResponse({"status":"failure","msg":"u should medically fit to apply for this job"})     


class AgeValidationMiddleware():
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        if request.path == "/job2/": 
            print(request.method,"job2 age") 
            print("age mw triggered")          
            incoming_data=json.loads(request.body)            
            age=int(incoming_data.get("age"))
            print(age,"ageeee")
            if age >= 21:
                response=self.get_response(request) 
                print(response,"hellooooo")
                return response 
            return JsonResponse({"status":"failure","msg":"u should have atleast age of 21 to apply for this job"})     

