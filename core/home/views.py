from django.shortcuts import render


# Create your views here.
def get(request):
    context = {
        'path': request.path
    }
    return render(request, 'home/get', context)
