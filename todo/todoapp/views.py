from django.shortcuts import render,HttpResponse,redirect
from todoapp.models import TaskList
# Create your views here.

def contact_page(request):

    return HttpResponse("<h1>Hello from contact page!!!</h1>")

def home_page(request):

    #return redirect('/contact')
    t=TaskList.objects.all() #select * from todoapp_TaskList
    print(t)
    for x in t:#[obj1,obj2,obj3,obj4]
        #print(x)
        print("ID:",x.id)
        print("Title:",x.title)
        print("Due date:",x.due_dt)
        print("Complete:",x.is_completed)
        print("Active:",x.is_active)
        print()
    return render(request,'todoapp\dashboard.html')

def student_page(request):

    return HttpResponse("welcome to student page!!!")

def product_page(request):

    return HttpResponse("welcome to product page!!!")

def placement_page(request):

    return HttpResponse("welcome to placement page!!!")

def add_task(request):
    print("Method Type:",request.method) #GET | POST

    if request.method=='POST':#GET==POST False | POST=POST=>True
        #print("In if section")
        #return HttpResponse("Insert data in database")
        #Fetch form data
        t=request.POST['title']
        d=request.POST['det']
        dt=request.POST['duedt']
        print("Title",t)
        print("Details",d)
        print("Date",dt)
        t=TaskList.objects.create(title=t,detail=d,due_dt=dt)#object created
        t.save()#object saved
        return HttpResponse("Data inserted succefully into database table")
       
    else: 
        print("In else section")   
        return render(request,'todoapp/addtask.html')
    
def dtl(request):
    context={}
    context['a']=100
    context['b']=50
    context['user']='dada'
    context['l']=[10,20,30,40,50,60]
    return render(request,'todoapp/dashboard.html',context)