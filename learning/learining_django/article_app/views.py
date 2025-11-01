from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Article
from django.views import View
from .froms import create_articleform
from django.shortcuts import render, redirect

class ArticleListView(ListView):
    model = Article
    template_name = "articlelist.html"
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.all()

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

class createArticle(View):
    values = {'title': 'Create Article', 'author': 'lohieth'}
    form = create_articleform(values)

    def get(self, request, *args, **kwargs):
        return render(request, 'create_article.html', {'form': self.form})
    
    def post(self, request, *args, **kwargs):
        form = create_articleform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article-list')
        return render(request, 'create_article.html', {'form': form})

