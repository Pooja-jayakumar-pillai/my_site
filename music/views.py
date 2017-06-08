from __future__ import unicode_literals

from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from django.shortcuts import render, redirect

# Create your views here.
from music.models import Album, Song


class AlbumListView(ListView):
    model = Album
    #template_name= 'album_list.html'


class AlbumDetailView(DetailView):
    model = Album
    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView , self).get_context_data(**kwargs)
        songs = Song.objects.filter(album=context['album'])
        context["songs"] = songs
        return context

    def post(self,request,*args,**kwargs):
        name = self.request.POST['name']
        artist = self.request.POST['artist']
        album = Album.objects.get(id=self.kwargs['pk'])
        song = Song(name=name,artist=artist,album=album)
        song.save()
        return redirect('album_detail',album.id)
class AlbumCreateView(CreateView):
    model = Album
    fields = ['name','img','genre']
    success_url = '/music/'
