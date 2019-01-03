from django.urls import path
from articles import views

urlpatterns = [
    path('', views.ArticleListView.as_view()),
    path('<pk>', views.ArticleDetailView.as_view())
]