from typing import Counter
from django.shortcuts import render,redirect
from . import models
from .models import Book
from django.contrib.auth.decorators import login_required
from .models import *
from datetime import *
from django.urls import reverse

# Create your views here.
"""Views for the very first page of the library system"""
def index(request):
    return render(request, 'books/index.html')

"""Defining views for the home page"""
@login_required
def home(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'books/home.html', context)

"""Defining views for the search_book page"""
@login_required
def search_book(request):
    notifications(request)
    if request.method == "POST":
        searched = request.POST['searched']
        books = Book.objects.filter(title__icontains=searched)
        context = { 'searched':searched,'books':books }
        return render(request, 'books/search_book.html', context)
    else:
        return render(request, 'books/search_book.html')

"""Defining views for the borrow page"""
@login_required
def borrow(request, book_id):
    clicked = Book.objects.get(id = book_id)
    all_books = Book.objects.all()
    books = Book.objects.filter(title__icontains=clicked)
    # determining how many times a user has borrowed books
    count = RequestedBook.objects.filter(user = request.user).count()
    context = {'clicked':clicked, 'books':books, 'all_books':all_books,'count':count}
    return render(request, 'books/borrow.html',context)

def get_return_date():
  return datetime.now() + timedelta(days = 14)

def book_time_limit():
  return datetime.now() + timedelta(hours=6)

"""Views for the confirm borrow"""
@login_required
def confirm_borrow(request,id):
    book = Book.objects.get(id=id)
    borrower = Borrower(first_name=request.user.first_name,last_name=request.user.last_name,username=request.user.username,book_name=book.title)
    borrower.save()
    requested_book = RequestedBook(book_name = book.title ,pickup_time = book_time_limit(),return_date= get_return_date(),borrower=request.user,user=request.user)
    requested_book.save()
    book.status = False
    book.save()
    return redirect('/requested_book/')


@login_required
def remove_book(request,id):
    remove = RequestedBook.objects.get(id=id)
    remove.delete()
    new = Book.objects.get(title=remove.book_name)
    new.status = True
    new.save()
    return redirect(request.META['HTTP_REFERER'])
    
@login_required
def profile(request):
    return render(request, 'books/returned_book.html')



"""Views for notifications"""
@login_required
def notifications(request):
    fine = Book.objects.all() 
    notice = Returned_book.objects.filter(user = request.user)
    for returned in notice:
        if returned.date_of_return > returned.return_date + timedelta(days=3):
            context = {'fine5000': 'you have a fine of 5000 UGX for' + str(returned.book_name)}
            fine.status = False
            return render(request,'books/notifications.html',context)
        elif returned.date_of_return > returned.return_date + timedelta(days=10):
            context = {'fine15000':'you have a fine of 15000 UGX ' + str(returned.book_name)}
            fine.status = False
            return render(request,'books/notifications.html',context)
        elif returned.date_of_return < returned.return_date + timedelta(days=3):
            context = {'nofine':' you dont have any fines'}
            return render(request,'books/notifications.html',context)
    
    context = {'nofine':'   You dont have any fines'}
    return render(request,'books/notifications.html',context)

@login_required
def requested_book(request):
    requested = RequestedBook.objects.filter(user = request.user)
    context = {'requested':requested}
    
    return render(request,'books/requested_book.html', context)


@login_required
def returned_book(request):
    return render(request, 'books/returned_book.html')
