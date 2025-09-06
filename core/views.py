from django.http import HttpResponse
import environ

env = environ.Env()

def hello(request):
    name = env('YOUR_NAME', default='stranger')
    return HttpResponse(f"Hello, {name}!")
