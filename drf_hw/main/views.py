from django.shortcuts import render
from django.forms import model_to_dict

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book, Author
from .serializers import *

# class BookApiView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all().values()
        return Response({'books': list(books)})
    
    def post(self, request):
        post_new = Book.objects.create(
            name = request.data['name'],
            dicription = request.data['dicription'],
            year_of_issue = request.data['year_of_issue'],
            author = request.data['author'],
            
        )

        return Response({'post': model_to_dict(post_new)})