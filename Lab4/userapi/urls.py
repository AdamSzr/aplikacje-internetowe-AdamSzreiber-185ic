from django.urls import path,include
from django.conf.urls import url
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('users',views.UserView)
router.register('posts',views.PostView)


urlpatterns = [
   # url('',views.UserView())
  #  path('user', include('userapi.urls')),
    path('',views.post_list,name='post_list'),
    path('api',include(router.urls)),
]
