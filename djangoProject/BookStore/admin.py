from django.contrib import admin
from BookStore.models import Author, Book, Publisher

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)

