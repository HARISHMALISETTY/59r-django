from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


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