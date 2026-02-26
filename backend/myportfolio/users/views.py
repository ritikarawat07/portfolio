from django.http import HttpResponse

def user_test(request):
    return HttpResponse("Users working")