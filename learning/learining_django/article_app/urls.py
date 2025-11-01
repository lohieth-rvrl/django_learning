from django.urls import path
# from .views import ArticleListView, ArticleDetailView
from . import views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article-list"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="article-detail"),
    path("create/", views.createArticle.as_view(), name="create-article"),
]
