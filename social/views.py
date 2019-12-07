from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Profile,Post,FollowUser,Comment,Like
from django.db.models import Q
from django.views.generic.edit import UpdateView,CreateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.views.generic import UpdateView,CreateView,TemplateView,ListView,DetailView

# Create your views here.
def home(request):
    return render(request,'social/home.html')

def about(request):
    return render(request,'social/about.html')

def contact(request):
    return render(request,'social/contact.html')

def follow(request,pk):
    user = profile.objects.get(pk=pk)
    FollowUser.objects.create(Profile=user, followe_by = request.user.profile)
    return HttpResponseRedirect(redirect_to="/social/profile")

class ProfileUpdateView(UpdateView):
    model = Profile
    fields=['name','age','address','gender','status','Mobile_no','Desciption','pic']

class PostCreateView(CreateView):
    model = Post
    fields = ['Title','subject','Desciption']
    def form_valid(self, form):
        self.object = form.save()
        self.object.upload_by = self.request.user.first_name
        self.object.save()
        return HttpResponceRedirect(self.get_success_url())

class PostListView(ListView):
    model = Post
    def get_queryset(self,*args, **kwargs):
        si = self.request.GET.get('si')
        if si == None:
            si = ''
        post_list = Post.objects.filter(Q(upload_by  = self.request.user.username)).filter(Q(subject__icontains=si) | Q(msg__icontains=si)).order_by("-id")
        return post_list
class PostDetailView(DetailView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post

class ProfileListView(ListView):
    model = Profile
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ''
        return Post.objects.filter(Q(upload_by = self.request.user.username)).filter(Q(name__icontains=si) | Q(address__icontains=si)).order_by("-id")

class ProfileDetailView(DetailView):
    model = Profile
