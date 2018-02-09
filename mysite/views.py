from django.shortcuts import render
from blog.models import Post
from board.models import Board
from django.http import HttpResponse
import datetime

def home(request):
    posts = Post.objects.order_by('-created_date')[0:5]
    boards = Board.objects.order_by('-created_date')[0:5]
    return render(request, 'home.html',{'posts':posts,'boards':boards})