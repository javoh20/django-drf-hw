from rest_framework import serializers
from .models import *

class BookModel:
    def __init__(self, name, discription, year_of_issue, author):
        self.name = name
        self.discription = discription
        self.year_of_issue = year_of_issue
        self.author = author


class BookSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 50)
    discription = serializers.CharField()
    year_of_issue = serializers.DateField()
    author = serializers.CharField()    