from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    template = 'home/home_page.html'
    return render_to_response(template)

def user(request):
    log= 'home/user_login.html'
    return render_to_response(log)


def clog(request):
    p = 'home/company_login.html'
    return render_to_response(p)
