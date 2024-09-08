from django.db import models

class Author(models.Model):
    # Field to store the author's name
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    # Field to store the book's title
    title = models.CharField(max_length=200)
    # Field for the year of publication
    publication_year = models.PositiveIntegerField()
    # Foreign key linking to the Author model
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title