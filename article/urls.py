from django.urls import path
from article import views

urlpatterns = [
    path('get-article',views.getArticle,name="get-article"),
    path('detail-article/<str:pk>',views.detailArticle,name="detail-article"),
    path('post-article',views.postArticle,name="post-article"),
    path('update-article/<str:pk>',views.updateArticle,name="update-article"),
    path('delete-article/<str:pk>',views.deleteArticle,name="delete-article"),
    path('list',views.ApiBlogListView.as_view(),name="list"),
]
