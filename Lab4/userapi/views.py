from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import generics

from .models import User
from .serializers import UserSerializer
from .models import Post
from .serializers import PostSerializer

# Create your views here.
def home_view(request,*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")

class UserView(viewsets.ModelViewSet): 
    # https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    # The actions provided by the ModelViewSet class are .list(), .retrieve(), .create(), .update(), .partial_update(), and .destroy().
    queryset = User.objects.all()
    serializer_class= UserSerializer
    # Because ModelViewSet extends GenericAPIView, you'll normally need to provide at least the queryset and serializer_class attributes. For example:

class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def post_list(request):
    posts = Post.objects.all()
    return render(request,'userapi/post_list.html',{'posty':posts})

