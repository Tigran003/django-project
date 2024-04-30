from django.shortcuts import render
from django.views.generic import ListView

from  .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'blogapp/article_list.html'
    context_object_name = 'articles'
    queryset = (
        Article.objects
        .select_related('author')
        .prefetch_related('articles')
        .all()
    )


    def get_queryset(self):

        return Article.objects.select_related('author', 'category').prefetch_related('tags').defer('content')