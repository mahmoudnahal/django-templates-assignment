from django.shortcuts import render
from datetime import datetime


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