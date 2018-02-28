from django.shortcuts import render
from board.models import Board, Category, File, Image
from django.shortcuts import redirect, get_object_or_404
from board.forms import BoardForm, FileForm, ImageForm

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
    images = board.image_set.all()
    return render(request, 'board/post_detail.html',{'board':board, 'categories':categories,'files':files, 'images':images})

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

            upimgs = request.FILES.getlist('image')
            for upimgs in upimgs:
                image = Image()
                image.image = upimgs
                image.post = post
                image.save()

            return redirect('board:post_detail', pk=post.pk)
    else:
        form = BoardForm()
        file = FileForm()
        image = ImageForm()

    return render(request, 'board/post_edit.html',{'form':form, 'categories':categories, 'file': file, 'image': image})

def post_edit(request,pk):
    categories = Category.objects.all()
    post = get_object_or_404(Board, pk=pk)
    getfile = post.file_set.all()
    getimage = post.image_set.all()

    if request.method == 'POST':
        form = BoardForm(request.POST, instance=post)
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

            upimgs = request.FILES.getlist('image')
            for upimgs in upimgs:
                image = Image()
                image.image = upimgs
                image.post = post
                image.save()

            return redirect('board:post_detail', pk=post.pk)
    else:
        form = BoardForm(instance=post)
        file = FileForm(instance=getfile)
        image = ImageForm(instance=getimage)

    return render(request, 'board/post_edit.html',{'form':form, 'categories':categories, 'file':file,'image':image})
