from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    
)
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)


class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post
    
class PostDetailView(DetailView):
        template_name = "posts/detail.html"
        model = Post
        
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def test_func(self):
        #must be T or F
        post = self.get_object() 
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")


    def test_func(self):
        #must be T or F
        post = self.get_object() 
        return post.author == self.request.user


class PasswordChangeView(UpdateView):
    template_name = "registration/password_change_form.html"

    
    
    
class PasswordChangeDoneView(UpdateView):
    email_template_name = "registration/password_reset_email.html"

# class PasswordResetView(UpdateView):
#     reset_template = "registration/password_reset_form.html"



