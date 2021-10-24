from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    # email = request.GET['email']
    send_mail(
        'otp for verifactions',
        "testing i am inayat",
        settings.EMAIL_HOST_USER,
        ['irasool037@gmail.com'],
        fail_silently=False
    )
    print("it is working")
    return render(request,'home.html')

    # return HttpResponse("hello it testing")