from django.shortcuts import render

from crud import models
from django.http import HttpResponse,HttpResponseRedirect
from crud.forms import NewBookForm,SearchForm

def searchBook(request):
    form =SearchForm()
    res = render(request,'crud/search_book.html',{'form':form})
    return res

def search(request):
    form = SearchForm(request.POST)
    books =models.Book.objects.filter(title= form.data['title'])
    res = render(request, 'crud/search_book.html', {'books':books, 'form':form})
    return res


def deleteBook(request):
    bookid = request.GET['bookid']
    book =models.Book.objects.get(id=bookid)
    book.delete()
    return HttpResponseRedirect('view-books')

def editBook(request):
    book =models.Book.objects.get(id=request.GET['bookid'])
    fields = {'title': book.title,'price': book.price, 'author': book.author, 'publisher': book.publisher}
    form = NewBookForm(initial=fields)
    res = render(request,'crud/edit_book.html', {'form': form, 'book': book})
    return res

def edit(request):
    if request.method=="POST":
        form=NewBookForm(request.POST)
        book=models.Book()
        book.id=request.POST['bookid']
        book.title = form.data['title']
        book.price = form.data['price']
        book.author= form.data['author']
        book.publisher = form.data['publisher']
        book.save()
    return HttpResponseRedirect('view-books')


def viewBooks(request):
    books =models.Book.objects.all()
    res=render(request,'crud/view_book.html',{'books':books})
    return res

def newBook(request):
    form = NewBookForm()
    res = render(request,'crud/new_book.html',{'form':form})
    return res

def add(request):
    if request.method == "POST":
        form = NewBookForm(request.POST)
        book =models.Book()
        book.title= form.data['title']
        book.price = form.data['price']
        book.author = form.data['author']
        book.publisher = form.data['publisher']
        book.save()
    s="Record Stored <br> <a href='/crud/view-books'> View All Books</a>"
    return HttpResponse(s)