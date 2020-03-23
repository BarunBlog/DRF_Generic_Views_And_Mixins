
from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails, GenericAPIView

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>/',article_detail),
    
    path('article_class/', ArticleAPIView.as_view()),
    path('detail_class/<int:id>/', ArticleDetails.as_view()),
    path('generic_article/<int:id>/', GenericAPIView.as_view())
]