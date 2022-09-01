from posixpath import basename
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')

urlpatterns = [
    path('viewsets/', include(router.urls)),
    path('viewsets/<int:pk>', include(router.urls)),
    # path('article/', views.article_list),
    path('article/', views.ArticleAPIView.as_view()),
    path('detail/<int:id>/', views.ArticleDetails.as_view()),
    path('generic/article/<int:id>/', views.GenericAPIView.as_view()),
    # path('detail/<int:pk>/', views.article_detail)    
]
