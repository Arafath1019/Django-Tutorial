from django.shortcuts import render, HttpResponse

def home(request):
    name = ["fahad", "hossain", "fahmida", "farhana"]
    context = {
        "name": name
    }
    return render(request, 'home.html', context)