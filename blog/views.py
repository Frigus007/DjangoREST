from django.shortcuts import render,redirect
from .forms import add_blog,comment
from .models import Blog,Hotels,Comments
from django.views import generic
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()

    return render(response, "registration/register.html", {"form":form})
def home(request):
    return render(request,'blog/index.html')

@login_required(login_url='/login/')
def create_blog(request):
    if request.method=='POST':
        form=add_blog(request.POST,request.FILES)

        if form.is_valid():
            blog=form.save(commit=False)
            blog.save()
            request.user.blog.add(blog)
            return redirect('/')
        return redirect('/')
    else:
        form=add_blog()
        return render(request,'blog/add_blog.html',{'form':form})
def display(request):
    blog=Blog.objects.all()
    print(blog)

    for i in blog:
        print(i.uploaded_by)


    return render(request,'blog/list.html',{'blog':blog})
@login_required(login_url='/login/')
def detail(request,pk):
    blog = Blog.objects.get(pk=pk)
    come = Comments.objects.all().filter(blog_id=pk)

    if request.method=='POST':
        form=comment(request.POST)
        if form.is_valid():
            blog_id=request.POST.get("pk", "")
            comm=form.save(commit=False)
            #print(blog_id)
            comm.blog_id=blog_id
            comm.save()
            form = comment()
            return render(request,'blog/detail.html',{'blog':blog,'pk':pk,'come':come,'form':form})
            #return redirect('/home')
    else:
        form = comment()
        #comm=Comments.object.get()
        return render(request,'blog/detail.html',{'blog':blog,'pk':pk,'come':come,'form':form})

def contact(request):
    return render(request,'blog/contact.html')