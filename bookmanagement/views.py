from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

# 1. READ Operation: Display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

# 2. CREATE Operation: Add a new book
def book_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        
        # Save to database using Django ORM
        Book.objects.create(title=title, author=author, price=price)
        return redirect('book_list')
    return render(request, 'books/book_form.html')

# 3. UPDATE Operation: Modify a book's price
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.price = request.POST.get('price')
        book.save()  # Update record
        return redirect('book_list')
    return render(request, 'books/book_update.html', {'book': book})

# 4. DELETE Operation: Remove a book record
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()  # Delete record
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
