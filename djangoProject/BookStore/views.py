from django.shortcuts import render
from BookStore.models import Book
from BookStore.models import Author

from django.http import HttpResponse
from BookStore.forms import BookQueryForm
from datetime import datetime


# Create your views here.

def info(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>{}</td><td>{}</td></tr>'.format(k, v))
    return HttpResponse('<table>{}</table>'.format('\n'.join(html)))

def lista_aut(request):
    autores = Author.objects.all()
    ts = {'autores': autores}
    return render(request, 'AuthorList.html', ts)


def lista_liv(request):
    livros = Book.objects.all()
    ts = {'livros': livros}
    return render(request, 'BookList.html', ts)


def lista_liv_author(request, name):
    autor = Author.objects.get(name=name)
    livros = Book.objects.filter(authors=autor)
    ts = {'livros': livros}
    return render(request, 'BookListAutor.html', ts)


def liv_details(request, name):
    livro = Book.objects.get(title=name)
    ts = {'livro': livro}
    return render(request, 'BookDetail.html', ts)


def aut_details(request, name):
    autor = Author.objects.get(name=name)
    ts = {'autor': autor}
    return render(request, 'AuthorDetail.html', ts)


def booksearch(request):
    if 'query' in request.POST:
        query = request.POST['query']
        if query:
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'booklist.html',
                          {'boks': books, 'query': query})
        else:
            return render(request, 'booksearch.html', {'error': True})
    else:
        return render(request, 'booksearch.html', {'error': False})


def bookquery(request):
    if request.method == 'POST':
        form = BookQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            books = Book.objects.filter(title__icontains=query)
            return render(request, 'booklist.html',
                          {'boks': books, 'query': query})
        else:
            form = BookQueryForm()
        return render(request, 'bookquery.html', {'form': form})

def home(request):
    tparams = {
        'title': 'Home Page',
        'year': datetime.now().year,
    }
    return render(request, 'index.html', tparams)