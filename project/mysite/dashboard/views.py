from django.shortcuts import render_to_response

# Create your views here.
def log(request):
    return render_to_response('home/profile_page.html')


def dash(request):
    return render_to_response('home/dashboard.html')
