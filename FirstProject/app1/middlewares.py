import json 
from django.http import HttpResponse,JsonResponse
import re

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

# class MedicalFitMiddleWare():
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         print(request.method,"job2 mf")
#         if request.path =="/job2/": 
#             print("mf triggered")          
#             incoming_data=json.loads(request.body)            
#             medically_fit=incoming_data.get("medically_fit")
#             if medically_fit == "True":
#                 response=self.get_response(request) 
#                 print(response,"hellooooo")
#                 return response 
#             return JsonResponse({"status":"failure","msg":"u should medically fit to apply for this job"})     


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

class IntermediateValidationMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response        
    def __call__(self,request):
        if request.path=="/seat/":
            print("seattttt")
            incoming_data=json.loads(request.body)
            inter_result=incoming_data.get("inter_result")
            if inter_result:
                response=self.get_response(request)
                return response
            return JsonResponse({"status":"failure","msg":"u should pass intermediate atleast"})

class EamcetqualifyMiddleWare:
    def __init__(self,get_response):
        self.get_response=get_response        
    def __call__(self,request):
        if request.path=="/seat/":
            print("seattttt")
            incoming_data=json.loads(request.body)
            eamcet_result=incoming_data.get("eamcet_result")
            if eamcet_result:
                response=self.get_response(request)
                return response
            return JsonResponse({"status":"failure","msg":"u should qualify eamcet"})
class UsernameMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response        
    def __call__(self,request):
        if request.path=="/user/":            
            incoming_data=json.loads(request.body)
            user_name=incoming_data.get("username")
            user_name_valid=re.match(r"^[A-Za-z0-9_]{5,15}$",user_name)
            if user_name_valid:
                response=self.get_response(request)
                return response
            return JsonResponse({"status":"failure","msg":"invalid username"})
 
class PasswordMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response        
    def __call__(self,request):
        if request.path=="/seat/":
            print("seattttt")
            incoming_data=json.loads(request.body)
            eamcet_result=incoming_data.get("eamcet_result")
            if eamcet_result:
                response=self.get_response(request)
                return response
            return JsonResponse({"status":"failure","msg":"u should qualify eamcet"})
 
class Emailmiddleware:
    def __init__(self,get_response):
        self.get_response=get_response        
    def __call__(self,request):
        if request.path=="/seat/":
            print("seattttt")
            incoming_data=json.loads(request.body)
            eamcet_result=incoming_data.get("eamcet_result")
            if eamcet_result:
                response=self.get_response(request)
                return response
            return JsonResponse({"status":"failure","msg":"u should qualify eamcet"})
