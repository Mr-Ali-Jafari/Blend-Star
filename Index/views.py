from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from . import forms,models
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    md = models.Post.objects.all().order_by("-date")
    liked_posts = []
    if request.user.is_authenticated:
        liked_posts = request.user.like_set.values_list('post_id', flat=True)
    return render(request,"index/index.html",{"md":md,'liked_posts': liked_posts})



@login_required
def create_post(request):
    if request.method == "POST":
        form = forms.CreationPost(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            form.save()
            print("Saved Form Is SuccessFully")
            return redirect("index")
    
    form = forms.CreationPost()


    return render(request,"index/create_post.html",{
        "form":form
    })


@login_required
def like_post(request, post_id):
    post = get_object_or_404(models.Post, id=post_id)
    like, created = models.Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('index')


@login_required
def edit_post(request,pk):
    md = models.Post.objects.get(pk=pk)
    if request.method == "POST":
        form = forms.CreationPost(request.POST,instance=md)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            form.save()
        
        return redirect("index")
    form = forms.CreationPost(instance=md)
    return render(request,"index/edit_post.html",{"form":form})