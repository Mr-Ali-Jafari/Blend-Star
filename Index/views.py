from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from . import forms,models
from django.contrib.auth.decorators import login_required
from Account import models as account_model
# Create your views here.


def index(request):
    md = models.Post.objects.all().order_by("-date")
    liked_posts = []
    for i in md:
        user = i.user
        if request.user.is_authenticated:
            liked_posts = user.like_set.values_list('post_id', flat=True)


    return render(request,"index/index.html",{"md":md,'liked_posts': liked_posts})



@login_required(login_url="/account/login/")
def create_post(request):
    try:
        profile = request.user.profile
    except account_model.Profile.DoesNotExist:
        return redirect("c_e_profile")
    

    if request.method == "POST":
        form = forms.CreationPost(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user.profile
            form.save()
            print("Saved Form Is SuccessFully")
            return redirect("index")
        
    form = forms.CreationPost()


    return render(request,"index/create_post.html",{
            "form":form
        })



@login_required(login_url="/account/login/")
def like_post(request, post_id):
    try:
        profile = request.user.profile
    except account_model.Profile.DoesNotExist:
        return redirect("c_e_profile")
    
    post = get_object_or_404(models.Post, id=post_id)
    like, created = models.Like.objects.get_or_create(user=request.user.profile, post=post)
    if not created:
        like.delete()
    return redirect("detail_post",post_id)


@login_required(login_url="/account/login/")
def edit_post(request,pk):
    try:
        profile = request.user.profile
    except account_model.Profile.DoesNotExist:
        return redirect("c_e_profile")

    md = models.Post.objects.get(pk=pk)
    if request.method == "POST":
        form = forms.CreationPost(request.POST,instance=md)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user.profile
            form.save()
        
        return redirect("index")
    form = forms.CreationPost(instance=md)
    return render(request,"index/edit_post.html",{"form":form})





def detail_post(request,pk):

    
    md = models.Post.objects.get(pk=pk)
    comment_md = models.Comment.objects.filter(user=md.user).order_by("-date")
    liked_posts = []

    if request.user.is_authenticated:
            liked_posts = request.user.profile.like_set.values_list('post_id', flat=True)

    if request.method == "POST":
        form = forms.CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user.profile
            comment.post = md
            comment.save()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    form = forms.CommentForm()
    return render(request,"index/detail_post.html",{"form":form,"md":md,'liked_posts': liked_posts,"comment_md":comment_md})


