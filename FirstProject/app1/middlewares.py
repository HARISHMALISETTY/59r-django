import json 
from django.http import HttpResponse,JsonResponse
import re
from .models import User
# class Middleware:
#     def __init__(self,get_response):
#         print("server starrted by harish")
#         self.get_response=get_response

#     def __call__(self,request):      
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

# class SSCMiddleware():
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         if request.path=="/job1/":            
#             incoming_data=json.loads(request.body)            
#             ssc_status=incoming_data.get("ssc_status")
#             if ssc_status == "True":
#                 response=self.get_response(request) 
#                 print(response,"hellooooo")
#                 return response 
#             return JsonResponse({"status":"failure","msg":"u should qualify ssc to apply for this job"})     

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


# class AgeValidationMiddleware():
#     def __init__(self,get_response):
#         self.get_response=get_response
#     def __call__(self,request):
#         if request.path == "/job2/": 
#             print(request.method,"job2 age") 
#             print("age mw triggered")          
#             incoming_data=json.loads(request.body)            
#             age=int(incoming_data.get("age"))
#             print(age,"ageeee")
#             if age >= 21:
#                 response=self.get_response(request) 
#                 print(response,"hellooooo")
#                 return response 
#             return JsonResponse({"status":"failure","msg":"u should have atleast age of 21 to apply for this job"})     

# class IntermediateValidationMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response        
#     def __call__(self,request):
#         if request.path=="/seat/":
#             print("seattttt")
#             incoming_data=json.loads(request.body)
#             inter_result=incoming_data.get("inter_result")
#             if inter_result:
#                 response=self.get_response(request)
#                 return response
#             return JsonResponse({"status":"failure","msg":"u should pass intermediate atleast"})

# class EamcetqualifyMiddleWare:
#     def __init__(self,get_response):
#         self.get_response=get_response        
#     def __call__(self,request):
#         if request.path=="/seat/":
#             print("seattttt")
#             incoming_data=json.loads(request.body)
#             eamcet_result=incoming_data.get("eamcet_result")
#             if eamcet_result:
#                 response=self.get_response(request)
#                 return response
#             return JsonResponse({"status":"failure","msg":"u should qualify eamcet"})
# class UsernameMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response        
#     def __call__(self,request):
#         if request.path=="/user/":            
#             incoming_data=json.loads(request.body)
#             user_name=incoming_data.get("username")
#             user_name_valid=re.match(r"^[A-Za-z0-9_]{5,15}$",user_name)
#             if user_name_valid:
#                 response=self.get_response(request)
#                 return response
#             return JsonResponse({"status":"failure","msg":"invalid username"})
 
# class PasswordMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response        
#     def __call__(self,request):
#         if request.path=="/seat/":
#             print("seattttt")
#             incoming_data=json.loads(request.body)
#             eamcet_result=incoming_data.get("eamcet_result")
#             if eamcet_result:
#                 response=self.get_response(request)
#                 return response
#             return JsonResponse({"status":"failure","msg":"u should qualify eamcet"})
 
# class Emailmiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response        
#     def __call__(self,request):
#         if request.path=="/seat/":
#             print("seattttt")
#             incoming_data=json.loads(request.body)
#             eamcet_result=incoming_data.get("eamcet_result")
#             if eamcet_result:
#                 response=self.get_response(request)
#                 return response
#             return JsonResponse({"status":"failure","msg":"u should qualify eamcet"})

from django.http import HttpResponse

class CORSMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            if request.method == "OPTIONS":
                response = HttpResponse(status=200)
            else:
                response = self.get_response(request)

            # 🔒 SAFETY NET (THIS FIXES YOUR CRASH)
            if response is None:
                response = HttpResponse(status=500)

        except Exception:
            response = HttpResponse(status=500)

        # ✅ Always add CORS headers
        response["Access-Control-Allow-Origin"] = "http://127.0.0.1:3000"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"

        return response

class authMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        self.username_pattern = re.compile(r'^[a-zA-Z0-9_]{5,15}$')
        self.password_pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@#]{8,}$')
        self.email_pattern = re.compile(r'^[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,}$')
    def __call__(self,request):
        if request.path in ["/signup/", "/login/"] and request.method == "POST":
             try:
                data = json.loads(request.body)
             except json.JSONDecodeError:
                return JsonResponse({"error": "Invalid JSON data"}, status=400)
             if request.path == "/signup/":
                username = data.get("username")
                email = data.get("email")
                password = data.get("password")
                if not all([username, email, password]):
                    return JsonResponse({"error": "All fields are required"}, status=400)

                if not self.username_pattern.match(username):
                    return JsonResponse({"error": "Invalid username format"}, status=400)

                if not self.email_pattern.match(email):
                    return JsonResponse({"error": "Invalid email format"}, status=400)

                if not self.password_pattern.match(password):
                    return JsonResponse({"error": "Weak password"}, status=400)

                if User.objects.filter(username=username).exists():
                    return JsonResponse({"error": "Username already exists"}, status=400)

                if User.objects.filter(email=email).exists():
                    return JsonResponse({"error": "Email already exists"}, status=400)
 
             if request.path == "/login/":
                username = data.get("username")
                password = data.get("password")
                print(password)

                if not all([username, password]):
                    return JsonResponse({"error": "Username & password required"}, status=400)

                try:
                    user = User.objects.get(username=username)
                    print(user)
                except User.DoesNotExist:
                    return JsonResponse({"error": "Invalid username"}, status=401)

                if user.password != password:
                # if not check_password(password,user.password):
                    return JsonResponse({"error": "Invalid password"}, status=401)

        response=self.get_response(request)
        return response
