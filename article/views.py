from django.shortcuts import render
from article.models import Article
from article.serializers import ArticleSerializers
from rest_framework import decorators, status, permissions
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def getArticle(request):
    article = Article.objects.all()
    serializer = ArticleSerializers(article, many=True)
    return Response(serializer.data)

@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def detailArticle(request,pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializers(article,many=False)
    return Response(serializer.data)

@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
@decorators.parser_classes([MultiPartParser,FormParser])
def postArticle(request):
    serializer = ArticleSerializers(data=request.data)
    if serializer.is_valid():
        account = serializer.save()
        if account:
            return Response(serializer.data,status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAuthenticated])
@decorators.parser_classes([MultiPartParser,FormParser])
def updateArticle(request,pk):
    article = Article.objects.get(id=pk)
    serializer = ArticleSerializers(instance=article,data=request.data)
    if serializer.is_valid():
        articledata = serializer.save()
        if articledata:
            return Response(serializer.data,status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

@decorators.api_view(['DELETE'])
@decorators.permission_classes([permissions.IsAuthenticated])
def deleteArticle(request,pk):
    article = Article.objects.get(id=pk)
    deletearticle = article.delete()
    data = {}
    if deletearticle:
        data['success'] = "success delete"
        return Response(data)
    else:
        return Response("error")


class ApiBlogListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = (permissions.IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,OrderingFilter)
    search_filter = ('title','body')
