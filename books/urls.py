# from django.contrib import admin
# from django.urls import path 
# from . import views

# urlpatterns = [
#     path('books/', views.index , name='index')
# ]
from django.urls import path
from django.conf.urls import url


from . import views
app_name = 'books'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('register', views.UserFormView.as_view(), name='register'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add', views.BookCreate.as_view(), name='book-add'),
    path('<int:pk>/update', views.BookUpdate.as_view(), name='book-update'),
    path('<int:pk>/delete', views.BookDelete.as_view(), name='book-delete'),


]


    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('addbook/', views.AddBook.as_view(), name='AddBook'),