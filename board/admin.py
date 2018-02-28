from django.contrib import admin
from board.models import Board, File, Category, Image

# Register your models here.
admin.site.register(Image)
admin.site.register(File)
admin.site.register(Board)
