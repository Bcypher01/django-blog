from django.urls import path
from . import views

urlpatterns = [
    # path('article/', views.article_list),
    path('article/', views.ArticleAPIView.as_view()),
    path('detail/<int:id>/', views.ArticleDetails.as_view()),
    path('generic/article/', views.GenericAPIView.as_view()),
    # path('detail/<int:pk>/', views.article_detail)    
]
