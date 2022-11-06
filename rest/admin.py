from django.contrib import admin

# Register your models here.
from .models import Student ,Author ,Publish ,Book
admin.site.register(Student)
admin.site.register(Author)
admin.site.register(Publish)
admin.site.register(Book)