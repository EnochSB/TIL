from django.shortcuts import render, redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.
def index(request):
    images = Album.objects.all()
    form = AlbumForm()
    context = {
        'images': images,
        'form': form,
    }
    return render(request, 'albums/index.html', context)


def create(request):
    form = AlbumForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()

    return redirect('albums:index')