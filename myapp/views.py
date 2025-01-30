from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from .models import Post
from django.contrib import messages
# Create your views here.

def index(request):
    posts = Post.objects.all()

    if request.method == 'GET':
        category = request.GET.get('category')
        if category:
            posts = Post.objects.filter(category__icontains=category)

    return render(request, 'index.html', {'posts': posts})

def signup(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['password2']
        if(password == confirmation):
            if(User.objects.filter(username = username).exists()):
                messages.info(request,'Username already exists')
                return redirect('signup')
            elif(User.objects.filter(email = email).exists()):
                messages.info(request,'You already have an account')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')    
        else:
            messages.info(request,'password not matching')
            return redirect('signup')
    else:
        return render(request,'signup.html')
    
def login(request):
    if(request.method =="POST"):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username,email=email,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')    
    else:    
        return render(request,'login.html')    

def logout(request):
    auth.logout(request)
    return redirect('/')

def blog(request,id):
    post = get_object_or_404(Post, id=id)
    return render(request,'blog.html',{'post':post})

def post(request):
    if(request.method == 'POST'):
        title = request.POST['Title']
        description = request.POST['description']
        category = request.POST['category']
        image = request.FILES.get('image')
        new_post = Post(
            title=title,
            description=description,
            category=category,
            image=image if image else None , # Ensure image is None if no file was uploaded
            author = request.user
        )
        new_post.save();
        messages.info(request,'blog Posted successfully')
        return redirect('/')
    else:    
        return render(request,'post.html')