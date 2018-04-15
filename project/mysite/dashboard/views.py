from django.shortcuts import render_to_response

# Create your views here.
def log(request):
    return render_to_response('home/user_login.html')