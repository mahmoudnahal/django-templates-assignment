from django.shortcuts import render
from datetime import datetime
from .models import Person
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def index(request):
    context = {
        'first_name': 'mahmoud',
        'last_name': 'al nahal',
        'student_id': 1205485155,
        'address': 'Gaza, Palestine',
        'email': '',
        'birth_date': datetime(2002, 2, 5),
    }
    return render(request, 'pages/index.html', context)



def home(request):
    people = Person.objects.all()
    return render(request, 'pages/home.html', {'people': people})




def student_add(request):
    if request.method == 'POST':
       # الكائنات اللي بتمثل البيانات القادمة من المتصفح: request.POST للنصوص و request.FILES للملفات
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'pages/student_form.html', {'form': form})

def student_list(request):
    #عشان اعرض البيانات هين
    students = Student.objects.all()
    return render(request, 'pages/student_list.html', {'students': students})