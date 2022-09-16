from re import A
from rest_framework.serializers import ModelSerializer
from .models import Article, User

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        # fields = ['id', 'title', 'author', 'email'] 
        fields = '__all__'
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        