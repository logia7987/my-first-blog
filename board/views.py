from django.shortcuts import render
from board.models import Board, Category, File
from django.shortcuts import redirect, get_object_or_404
from board.forms import BoardForm, FileForm

# Create your views here.
def post_list(request):
    ctgry = request.GET.get('category')
    if ctgry != None:
        posts = Board.objects.filter(category__name = ctgry)
    else:
        posts = Board.objects.all()

    categories = Category.objects.all()

    return render(request, 'board/post_list.html',{'posts':posts, 'categories':categories})

def post_detail(request, pk):
    categories = Category.objects.all()
    board = get_object_or_404(Board, pk=pk)
    files = board.file_set.all()
    return render(request, 'board/post_detail.html',{'board':board, 'categories':categories,'files':files})

def post_new(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = BoardForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            upfls = request.FILES.getlist('file')
            for upfls in upfls:
                file = File()
                file.file = upfls
                file.post = post
                file.save()

            return redirect('board:post_detail', pk=post.pk)
    else:
        form = BoardForm()
        file = FileForm()

    return render(request, 'board/post_edit.html',{'form':form, 'categories':categories, 'file':file})

def post_edit(request,pk):
    categories = Category.objects.all()
    post = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = BoardForm(instance=post)

    return render(request, 'blog/post_edit.html',{'form':form, 'categories':categories,})
