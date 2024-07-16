from django.shortcuts import render, redirect
from .models import Article
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

# Create your views here.
def home(request):
    articles_list = Article.objects.all()
    paginator = Paginator(articles_list, 1)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {"articles": articles}
    return render(request,"blog/home.html",context)
def detail(request, slug):
    context={
        "article" : Article.objects.get(slug=slug)
    }
    
    return render(request,"blog/detail.html",context)

def about(request):

        return render(request,"blog/about.html")

def contact(request):

        return render(request,"blog/contact.html")

def login(request):

        return render(request,"blog/login.html")



def registrationpage(request):
        form = CreateUserForm()
        context = {'form': form}

        if request.method == "POST":
               form = CreateUserForm(request.POST)
               if form.is_valid():
                 form.save()
                 return redirect('/accounts/login/')
        return render(request, "registration/signup.html", context)        

@login_required
def accounthome(request):

        return render(request,"registration/home.html")

    
        