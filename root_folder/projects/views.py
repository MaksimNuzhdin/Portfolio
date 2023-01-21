from django.shortcuts import render
from django.views.generic import DetailView
from .models import Article, Photo, Paragraphs
# Create your views here.
class Project(DetailView):
    model=Article
    
    
    template_name='./project.html'
    context_object_name='project_class'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        art=self.get_object()
        photo_list=Photo.objects.filter(photo_binding=art)
        paragraph_list=Paragraphs.objects.filter(par_binding=art)
        
        

        context['photo_list']=photo_list
        context['paragraph_list']=paragraph_list
        context['art']=art
        return context