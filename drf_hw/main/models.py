from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 30)
    surname = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Book(models.Model):
    name = models.CharField(max_length = 50)
    dicription = models.TextField()
    year_of_issue = models.DateField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self):
        return self.name