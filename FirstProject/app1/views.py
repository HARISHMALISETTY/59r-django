from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Students,Employees,Resolutions,UserDetails,User
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.hashers import make_password
import jwt
from django.conf import settings
from datetime import datetime, timedelta


# Create your views here.
def view1(request):
    print(request.method)
    return HttpResponse("hello world,iam from view1")
def view2(request):
    return HttpResponse("hello world,iam from view2")
def view3(request):
    return HttpResponse("hello world, iam from view3")
def view4(request):
    return JsonResponse({"name":"harish","message":"hello world"})
def view5(request):
    return JsonResponse({"status":"success","response":"welcome"})

def dynamicview(request):
    qp1=request.GET.get("name",'world') #getting query param from url
    return HttpResponse(f"hello {qp1}")

# json always allow object only 

def personInfo(request):
    name=request.GET.get("name","harish")
    city=request.GET.get("city","hyd")
    role=request.GET.get("role","Trainer")
    info={"name":name,"city":city,"role":role}
    return JsonResponse({"status":"success","data":info})
def temp1(request):
    return render(request,"./simple.html")
def temp2(request):
    return render(request,"./second.html")

students = [
    {
        "id": 1,
        "name": "Akhil",
        "age": 22,
        "gender": "Male",
        "course": "Python Full Stack",
        "city": "Hyderabad",
        "marks": 85
    },
    {
        "id": 2,
        "name": "Sravani",
        "age": 21,
        "gender": "Female",
        "course": "Data Science",
        "city": "Vijayawada",
        "marks": 90
    },
    {
        "id": 3,
        "name": "Rahul",
        "age": 23,
        "gender": "Male",
        "course": "MERN Stack",
        "city": "Bangalore",
        "marks": 78
    },
    {
        "id": 4,
        "name": "Divya",
        "age": 22,
        "gender": "Female",
        "course": "Django",
        "city": "Chennai",
        "marks": 88
    },
    {
        "id": 5,
        "name": "Kiran",
        "age": 24,
        "gender": "Male",
        "course": "AI & ML",
        "city": "Hyderabad",
        "marks": 92
    }
]


def studentsByCity(request,city):
    filteredData=[]

    for student in students:
        if student["city"].lower()==city.lower():
            filteredData.append(student)   
    len(filteredData)

    if len(filteredData)>0:
        return JsonResponse({"data":filteredData,"message":"students records successfully fetched"},status=200)
    elif len(filteredData)==0:
        print("no content")
        return JsonResponse({"data":filteredData,"message":"no contenr available as per ur requirement"},status=404)
    else:
        return JsonResponse({"error":"something went wrong"})

def studentsByMarks(request,marks):
    filteredData=[]
    for student in students:
        if student["marks"]>marks:
            filteredData.append(student)
    if len(filteredData)>0:
        return JsonResponse({"data":filteredData,"message":"students records successfully fetched"},status=200)
    elif len(filteredData)==0:
        return JsonResponse({"data":filteredData,"message":"no contenr available as per ur requirement"},status=404)
    else:
        return JsonResponse({"error":"something went wrong"})



ecommerce_products = [
    {
        "id": 1,
        "name": "iPhone 14",
        "category": "Electronics",
        "brand": "Apple",
        "price": 69999,
        "stock": 25,
        "rating": 4.6,
        "city": "Hyderabad"
    },
    {
        "id": 2,
        "name": "Samsung Galaxy S23",
        "category": "Electronics",
        "brand": "Samsung",
        "price": 74999,
        "stock": 30,
        "rating": 4.5,
        "city": "Bangalore"
    },
    {
        "id": 3,
        "name": "Nike Running Shoes",
        "category": "Footwear",
        "brand": "Nike",
        "price": 4999,
        "stock": 50,
        "rating": 4.3,
        "city": "Chennai"
    },
    {
        "id": 4,
        "name": "Levi's Jeans",
        "category": "Clothing",
        "brand": "Levi's",
        "price": 2999,
        "stock": 40,
        "rating": 4.1,
        "city": "Pune"
    },
    {
        "id": 5,
        "name": "Boat Wireless Earbuds",
        "category": "Accessories",
        "brand": "Boat",
        "price": 1999,
        "stock": 60,
        "rating": 4.4,
        "city": "Hyderabad"
    },
    {
        "id": 6,
        "name": "HP Pavilion Laptop",
        "category": "Electronics",
        "brand": "HP",
        "price": 58999,
        "stock": 15,
        "rating": 4.2,
        "city": "Delhi"
    },
    {
        "id": 7,
        "name": "Wooden Study Table",
        "category": "Furniture",
        "brand": "HomeTown",
        "price": 8999,
        "stock": 10,
        "rating": 4.0,
        "city": "Mumbai"
    },
    {
        "id": 8,
        "name": "Samsung 55-inch Smart TV",
        "category": "Electronics",
        "brand": "Samsung",
        "price": 45999,
        "stock": 20,
        "rating": 4.7,
        "city": "Bangalore"
    }
]

# practise path params and then work on the below task.

# 1.create api to fetch product details
#     a.by category  
#     b.by rating

#connection to database using pymysql.


def productByRating(request,rating):
    try:
        cnvrt_rating=float(rating)
        if request.method=="GET":
            print(request.GET)
            filteredData=[]
            for product in ecommerce_products:
                if product["rating"]>=cnvrt_rating:
                    filteredData.append(product)
            if len(filteredData)==0:
                msg="No products found"
            else:
                msg="Products fetched successfully"
            return JsonResponse({"status":"success","message":msg,"total no.of records":len(filteredData),"data":filteredData})
        return JsonResponse({"status":"failure","message":"only get methoda allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})

@csrf_exempt #will act as a decorator
def addStudent(request):
    try:
        if request.method=="POST":
            print("started")
            inputData=json.loads(request.body)
            print(inputData)

            Students.objects.create(stud_name=inputData["name"],
            stud_age=inputData["age"],
            stud_gender=inputData["gender"],
            stud_email=inputData["email"])

            return JsonResponse({"status":"success","msg":"record added successfully"},status=201)
        return JsonResponse({"status":"failure","msg":"only post method allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":"error occured"})

@csrf_exempt
def addEmployee(request):
    try:
        if request.method=="POST":
            print(request)
            print(request.method)
            print(request.body)
            
            inputData=json.loads(request.body)
            Employees.objects.create(emp_name=inputData["name"],
            emp_age=inputData["age"],
            emp_gender=inputData["gender"],
            emp_email=inputData["mail"])
            return JsonResponse({"status":"success","msg":"inserted succesfully"},status=201)
        return JsonResponse({"status":"failure","msg":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"status":"error","msg":"error occured"})
    
def getStudents(request):
    try:
        if request.method=="GET":  
            data=Students.objects.values() 
            final_result=list(data) 
            print(final_result)        
            return JsonResponse({"status":"success","msg":"recordsFetched successfully","data":final_result},status=200)
        return JsonResponse({"status":"failure","msg":"only post method allowed"},status=400)
    except Exception as e:
        return JsonResponse({"status":"error","msg":"error occured"},status=500)

def getStudentsByGender(request,gender):
    try:
        if request.method=="GET":
            data=list(Students.objects.filter(stud_gender=gender).values())
            print(data)
            return JsonResponse({"status":"success",
                                "msg":"records fetched successfully",
                                "data":data},status=200)
        return JsonResponse({"status":"failure","msg":"only get method allowed"},status=400)
    except Exception as e:
         return JsonResponse({"status":"error","msg":"error occured"},status=500)
        

def getStudentsByAge(request,Age):
    try:
        if request.method=="GET":
            data=list(Students.objects.filter(stud_age__lt=Age).values())
            print(data)
            return JsonResponse({"status":"success",
                                "msg":"records fetched successfully",
                                "data":data},status=200)
        return JsonResponse({"status":"failure","msg":"only get method allowed"},status=400)
    except Exception as e:
         return JsonResponse({"status":"error","msg":"error occured"},status=500)
@csrf_exempt
def UpdateStudentAgeById(request,ref_id):
    try:
        if request.method=="PUT": 
            data=json.loads(request.body)
            new_age=data["new_age"]
            update=Students.objects.filter(id=ref_id).update(stud_age=new_age)  
            print(update)    
            if update==0:
                msg="no record found to update"
            else:
                msg="record is updated successfully"     
            return JsonResponse({"status":"success",
                                "msg":msg},status=200)
        return JsonResponse({"status":"failure","msg":"only PUT method allowed"},status=400)
    except Exception as e:
         return JsonResponse({"status":"error","msg":"error occured"},status=500)




#__lt=--->lessthan
#__gt=---->greaterthan
#__lte=---->lessthanorequalto
#__gte=---->greaterthanorequalto



@csrf_exempt
def AddResolutions(request):
    try:
        if request.method != "POST":
            return JsonResponse({"error": "Only POST allowed"}, status=405)

        data = json.loads(request.body.decode("utf-8"))

        Resolutions.objects.create(
            person_name = data.get("name"),
            resolution = data.get("resolution"),
            Deadline_in_mnths = int(data.get("deadline")),
            lastYearResolutionSatus = data.get("status_of_lastyear"),
            lastYearAchievements = data.get("lastyear_acheivements")
        )

        return JsonResponse({
            "status": "success",
            "msg": "data inserted successfully"
        })

    except Exception as e:
        print("ERROR 👉", e)   # 🔥 THIS IS IMPORTANT
        return JsonResponse({
            "status": "error",
            "msg": str(e)
        }, status=500)

def getAllResolutions(request):
    try:
        if request.method != "GET":
            return JsonResponse(
                {"status": "failure", "msg": "Only GET method allowed"},
                status=405
            )
        data = list(Resolutions.objects.all().values())

        return JsonResponse({
            "status": "success",
            "msg": "Resolutions fetched successfully",
            "data": data
        }, status=200)

    except Exception as e:
        print("ERROR 👉", e)
        return JsonResponse({
            "status": "error",
            "msg": str(e)
        }, status=500)

@csrf_exempt
def updateResolution(request,ref_id):
    try:
        if request.method=="PUT": 
            data=json.loads(request.body)
            new_resolution=data["new_res"]
            update=Resolutions.objects.filter(id=ref_id).update(resolution=new_resolution)  
            print(update)    
            if update==0:
                msg="no record found to update"
            else:
                msg="resolution  is updated successfully"     
            return JsonResponse({"status":"success",
                                "msg":msg},status=200)
        return JsonResponse({"status":"failure","msg":"only PUT method allowed"},status=400)
    except Exception as e:
         return JsonResponse({"status":"error","msg":"error occured"},status=500)

@csrf_exempt
def job1(request):
    try:
        if request.method=="POST":
            return JsonResponse({"status":"success","msg":"job1 applied successfully"})
        return JsonResponse({"status":"failure","msg":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"status":"error","msg":"something went wrong"})

@csrf_exempt
def job2(request):
    try:
        if request.method=="POST":
            print(json.loads(request.body))
            return JsonResponse({"status":"success","msg":"job2 applied successfully"})
        return JsonResponse({"status":"failure","msg":"only post method allowed"})
    except Exception as e:
        print("errorrrrr")
        return JsonResponse({"status":"error","msg":"something went wrong"})
@csrf_exempt
def EngineeringSeat(request):
    try:
        if request.method=="POST":
            return JsonResponse({"status":"success","msg":"u r eligible for engineering seat"})
        return JsonResponse({"status":"failure","msg":"only post method allowed"})
    except Exception as e:
        print("errorrrrr")
        return JsonResponse({"status":"error","msg":"something went wrong"})


@csrf_exempt
def addUser(request):
    try:
        if request.method=="POST":            
            inputData=json.loads(request.body)
            UserDetails.objects.create(username=inputData["username"],
            password=inputData["password"],
            userEmail=inputData["email"])
            return JsonResponse({"status":"success","msg":"user created successfully"},status=201)
        return JsonResponse({"status":"failure","msg":"only post method allowed"})
    except Exception as e:
        return JsonResponse({"status":"error","msg":"error occured"})

@csrf_exempt
def signup(request):
    data = json.loads(request.body)
    hashed_password=make_password(data["password"])
    
    user = User.objects.create(
        username=data["username"],
        email=data["email"],
        password=hashed_password
    )

    return JsonResponse({
        "status": "success",
        "msg": "User registered successfully"
    }, status=201)

    
@csrf_exempt
def login(request):
    user_info=json.loads(request.body)
    user=user_info.get("username") 
    user_existing_info=list(User.objects.filter(username=user).values())
    user_role=user_existing_info[0].get("role")
    print(user_role)
    print(user_existing_info)
    payload={
            "user":user,
            "role":user_role,
            "email":user_existing_info[0].get("email"),
            "iat":datetime.utcnow(),
            "exp":datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRYTIME)
            }

    token=jwt.encode(payload,settings.JWT_SECRET_KEY,algorithm=settings.JWT_ALGORITHM) 

    return JsonResponse({

        "status": "success",
        "msg": "Login successful",
        "greetings":f"welcome {user}",
        "token":token
        
    })