"""
URL configuration for FirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import AddResolutions,UpdateStudentAgeById,getStudentsByAge,getStudentsByGender,getStudents,addEmployee,addStudent,view1,view2,view3,view4,view5,dynamicview,personInfo,temp1,temp2,studentsByCity,studentsByMarks,productByRating

urlpatterns = [
    path('admin/', admin.site.urls),
    path('view1/',view1),
    path('view2/',view2),
    path('view3/',view3),
    path('view4/',view4),
    path('view5/',view5),
    path('dmv/',dynamicview),
    path('person/',personInfo),
    path('show/',temp1),
    path('second/',temp2),
    path('students/<str:city>',studentsByCity),
    path('studentbymarks/<int:marks>',studentsByMarks),
    path('prodByRating/<str:rating>',productByRating),
    path('addStudent/',addStudent),
    path('addEmployee/',addEmployee),
    path('getStudents/',getStudents),
    path('getStudentsByGender/<str:gender>',getStudentsByGender),
    path('getStudentsByAge/<int:Age>',getStudentsByAge),
    path('studentageupdate/<int:ref_id>',UpdateStudentAgeById),
    path('Resolutions/',AddResolutions)
]



