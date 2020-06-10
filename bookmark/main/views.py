from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from .forms import BookmarkForm
from django.core.paginator import Paginator

# Create your views here.

def show(request):
    bookmark = Bookmark.objects
    bookmarks = Bookmark.objects.all()
    paginator = Paginator(bookmarks, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'show.html', { 'bookmarks': bookmarks, 'posts': posts })


def new(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = Bookmark()
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.site_url = form.cleaned_data['site_url']
            bookmark.save()
            return redirect('main:show')

    else:
        form = BookmarkForm()
    return render(request, 'new.html', {'form':form})


def edit(request, pk):

    bookmark = get_object_or_404(Bookmark, pk=pk)

    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            bookmark.site_name = form.cleaned_data['site_name']
            bookmark.site_url = form.cleaned_data['site_url']
            bookmark.save()
            return redirect('main:show')

    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'new.html', {'bookmark':bookmark, 'form':form})


def delete(request, pk):

    bookmark = get_object_or_404(Bookmark, pk=pk)

    if request.method == 'POST':
        bookmark.delete()
        return redirect('main:show')