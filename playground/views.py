from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# request -> response
# request handler


# map this function to a url such that any time
# the url is launched, this function will be called
def say_hello(request):
    # returns plain HttpResponse
    # return HttpResponse('Hello World')

    # returns html text
    return render(request, 'hello.html', {"name" : "Simon"})
