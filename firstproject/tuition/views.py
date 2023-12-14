from django.shortcuts import render
from .models import Contact, Post
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data["name"]
            # phone = form.cleaned_data["phone"]
            # content = form.cleaned_data["content"]
            # obj = Contact(name= name, phone=phone, content=content)
            # obj.save()
            form.save()
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})

def postview(request):
    post = Post.objects.all()
    return render(request, "tuition/postview.html", {"post": post})