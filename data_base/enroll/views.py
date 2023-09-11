from django.shortcuts import render
from .models import Students


# Create your views here.
def studentinfo(request):
    stud = Students.objects.get(pk=2)

    return render(request, 'enroll/index.html', {
        'stu': stud
    })
