from django.shortcuts import render, redirect
from django.views.generic import CreateView,DetailView,DeleteView
from Posts.models import Createpost
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from rest_framework import filters, generics
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

class Postcreateview(LoginRequiredMixin,CreateView):
    model = Createpost
    fields = ['title','content']
    template_name='Create_Post.html'
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class Postdetailview(LoginRequiredMixin,DetailView):
    model=Createpost
    template_name='Post_detailview.html'

class Postdeleteview(LoginRequiredMixin,DeleteView):
    model= Createpost
    template_name='Delete_post.html'
    success_url ="/"
    
class Searchposts(generics.ListAPIView):
    querry=Createpost.objects.all()
    #serializer_class = CreatepostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','content','author__username']



