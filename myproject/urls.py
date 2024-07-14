"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path
from myapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('item_list/', views.item_list),
    path('item_post/', views.item_post),
    path('book_list/',views.book_list),
    path('book_post/', views.book_post),
    path('book_delete/<int:pk>/',views.book_delete),
    path('book_update/<int:pk>/',views.book_update),
    path('book_id/<int:pk>/',views.book_id),
    path('book_search/book_name', views.book_search),

    
]



