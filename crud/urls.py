from django.urls import path
from crud import views

urlpatterns = [
    path('view-books',views.viewBooks),
    path('edit-book', views.editBook),
    path('delete-book', views.deleteBook),
    path('search-book', views.searchBook),
    path('new-book/', views.newBook),
    path('add', views.add),
    path('edit', views.edit),
    path('search', views.search),

]
