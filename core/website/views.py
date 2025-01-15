from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm
from accounts.models import User, Profile

# Index page
def index_view(request):
    """ Summary:
        Main page that contains contact form and other stuff.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد.")
        else:
            messages.error(request, ("پیام شما ارسال نشد!"))
            
    form = ContactForm()
    context = {"form": form}
    return render(request, "website/index.html", context)

# About page
def about_view(request):
    mamad = User.objects.get(email=("mamad@admin.com"))
    arashk = User.objects.get(email=("arashk@admin.com"))
    m_profile = Profile.objects.get(user=mamad)
    a_profile = Profile.objects.get(user=arashk)
    context = {
        "m_profile" : m_profile,
        "a_profile" : a_profile,
        }
    return render(request, "website/about.html", context)

# Contact page
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد.")
        else:
            messages.error(request, ("پیام شما ارسال نشد!"))
    
    mamad = User.objects.get(email=("mamad@admin.com"))
    arashk = User.objects.get(email=("arashk@admin.com"))
    m_profile = Profile.objects.get(user=mamad)
    a_profile = Profile.objects.get(user=arashk)
    
    form = ContactForm()
    context = {
        "form": form,
        "m_profile" : m_profile,
        "a_profile" : a_profile,
        }
    return render(request, "website/contact.html", context)
