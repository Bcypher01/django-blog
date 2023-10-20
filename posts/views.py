from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view, APIView
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404


class PostViewset(viewsets.ViewSet):
    def list(self, request: Request):
        queryset = Post.objects.all()
        serializer = PostSerializer(instance=queryset, manay=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request: Request, pk=None):
        post = get_object_or_404(Post, pk=pk)

        serializer = PostSerializer(instance=post)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


# class PostListCeateView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     # A View for creating and listing posts
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get(self, request: Request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request: Request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class PostRetrieveUpdateDeleteView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def get(self, request: Request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request: Request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request: Request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
