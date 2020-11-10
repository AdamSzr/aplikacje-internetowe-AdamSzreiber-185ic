from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), #Jak widzisz, teraz przyporządkowujemy widok (view) o nazwie post_list do strony głównej
    #name='post_list jest nazwą URL, która będzie używana do zidentyfikowania widoku. Nazwa może być taka sama jak nazwa widoku albo kompletnie inna. W projekcie będziemy później używać nazw URL, więc ważne jest nazwanie każdego URL-a w aplikacji. Powinnyśmy również starać się używać nazw URL unikalnych i prostych do zapamiętania.
    path('post/<int:pk>',views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]