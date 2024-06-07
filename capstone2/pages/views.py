from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, DetailView
from .models import Post
from django.urls import reverse
from django.shortcuts import render
from .utils import magic




from .forms import CreateForm
class HomePageView(TemplateView):
    template_name = "pages/home.html"
    
    
class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    
    
    
    #list
class Create(CreateView):
    models = Post
    template_name = "pages/create.html"
    form_class = CreateForm
    
    def get_success_url(self) -> str:
        return reverse('list')


class ListPosts(ListView):
    model = Post
    template_name = "pages/list.html"
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.all()
    
    
class PostDetail(DetailView):
    model = Post
    template_name = "pages/detail.html"
    context_object_name = 'post'
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
        
def sortie(request):
    if request.method == 'POST':
        input_paragraph = request.POST.get('paragraph', '')
        output = magic(input_paragraph)
        return render(request, 'pages/sorted_paragraph.html', {'result': output})
    else:
        return render(request, 'pages/submit_paragraph.html')