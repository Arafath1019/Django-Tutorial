from django.shortcuts import render, HttpResponse
from tuition.models import Contact

def home(request):
    name = ["fahad", "hossain", "fahmida", "farhana"]
    context = {
        "name": name
    }
    return render(request, 'home.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        content = request.POST["content"]
        obj = Contact(name= name, phone=phone, content=content)
        obj.save()
    
    return render(request, "contact.html")