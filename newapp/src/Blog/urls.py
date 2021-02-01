from django.urls import path
from .views import article_form_view, article_list_view,article_details_view, ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView,HomeDetailView

app_name = "Blog"

urlpatterns = [
    path('details/<int:id>/', ArticleDetailView.as_view(), name = "article-details"),
    path('list/',article_list_view ),
    path('', HomeDetailView.as_view(template_name = 'home.html'), name = "article-list"),
    path('<int:id>/', HomeDetailView.as_view(), name="home-detail-view"),
    path('create/', ArticleCreateView.as_view(), name = "article-create"),
    path('details/<int:id>/update/',ArticleUpdateView.as_view(), name = "article-update" ),
    path('details/<int:id>/delete/',ArticleDeleteView.as_view(), name = "article-delete")
]