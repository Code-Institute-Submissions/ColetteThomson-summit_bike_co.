from django.urls import path
from . import views

# urls paths for views: 'ArticleList' and 'ArticleContent'
urlpatterns = [
    # blank path to indicate default as home page
    path('', views.ArticleList.as_view(), name='article_list'),
    # 'slug' keyword matches 'slug' parameter in get method of ArticleContent
    # path converter (slug) if matched to return a string, if not a 404 message
    path('<slug:slug>/', views.ArticleContent.as_view(),
         name='article_content'),
    # number of likes using slug (from article_content.html)
    path('like/<slug:slug>/', views.ArticleLike.as_view(),
         name='article_like'),
]
