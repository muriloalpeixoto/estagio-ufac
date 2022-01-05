from django.shortcuts import render

# main/views.py

from django.contrib import messages
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

# Create your views here.

from estagio.main.models import (
    Post,
    Category,
    Project,
    Contact,
)

from estagio.main.forms import ContactForm

class ProjectListView(ListView):
    model = Project
    paginate_by = 5
    template_name = 'pages/projects.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'pages/project_details.html'


class BlogListView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'pages/home.html'
    context_object_name = 'posts'
    ordering = ['-created_on']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__slug__contains=category
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "pages/category_list.html", context)


class ContactFormView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        m = Contact(
            name=name,
            email=email,
            message=message,
        )
        m.save()

        messages.success(self.request, 'Your message has been sent.')

        return super().form_valid(form)


class AboutView(TemplateView):
    template_name = 'pages/about.html'