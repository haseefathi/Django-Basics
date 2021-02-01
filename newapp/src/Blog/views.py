from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import ArticleModelForm
from .models import Article
from django.views import View

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.

class HomeObjectMixin(object):
    model = Article
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


class HomeDeleteView(HomeObjectMixin,View):
    template_name = 'article_delete.html'

    def get(self, request,  *args, **kwargs):
        context = {}
        obj = self.get_object()
        
        if obj is not None:
            context['object'] = obj 
        return render(request, self.template_name, context)

    def post(self, request,  *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            print("Deleting object")
            obj.delete()
            context['object'] = None
            return redirect('/art/homelist/')
        return render(request, self.template_name, context)

class HomeUpdateView(View):
    template_name = 'article_update.html'
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Article, id=id)
        return obj

    def get(self, request,  *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ArticleModelForm(instance = obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request,  *args, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = ArticleModelForm(request.POST, instance = obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class HomeCreateView(View):
    template_name = 'article_create.html'
    def get(self, request,  *args, **kwargs):
        
        form = ArticleModelForm()
        context = {"form": form}
        return render(request, self.template_name , context)
    def post(self, request,  *args, **kwargs):
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = ArticleModelForm()
        context = {"form": form}
        return render(request, self.template_name , context)
    


class HomeListView(View):
    template_name = 'article_list.html'
    queryset = Article.objects.all()
    def get_queryset(self):
        return self.queryset
    def get(self, request, *args, **kwargs):
        context = {'object_list': self.get_queryset() }
        return render(request, self.template_name, context)


class MyListView(HomeListView):
    queryset = Article.objects.filter(id=1)


class HomeDetailView(View):
    template_name = 'article_details.html'
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Article, id = id)
            context["object"] = obj
        return render(request, self.template_name , context)

class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id = id_)

    def get_success_url(self):
        return reverse("Blog:article-list")

class ArticleCreateView(CreateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    template_name = 'article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return (get_object_or_404(Article, id = id_))




class ArticleListView(ListView):
    template_name = 'article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'article_details.html'
    queryset = Article.objects.all()
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return (get_object_or_404(Article, id = id_))





def article_form_view(request, *args, **kwargs):
    form = ArticleModelForm()
    if request.method == "POST":
        form = ArticleModelForm(request.POST)
        if form.is_valid():
            Article.objects.create(**form.cleaned_data)
            form = ArticleModelForm()
    context = {
        "form": form
    }
    return render(request, 'form.html', context)

def article_list_view(request, *args, **kwargs):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, 'article_list.html', context)

def article_details_view(request, id):
    obj = Article.objects.get(id = id)
    context = {
        "object": obj
    }
    return render(request, 'article_details.html', context)


