from django.db import models


# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class PersonInfo(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(max_length=10)
    gender = models.BooleanField()
    book_id = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.age, self.name, self.gender, self.book_id_id