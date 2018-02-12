from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from blog.models import Post
from board.models import Board
from django.http import HttpResponse
import datetime

def home(request):
    posts = Post.objects.order_by('-created_date')[0:5]
    boards = Board.objects.order_by('-created_date')[0:5]
    return render(request, 'home.html',{'posts':posts,'boards':boards})

class UserRegister(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserRegisterDone(TemplateView):
    template_name = 'registration/register_done.html'