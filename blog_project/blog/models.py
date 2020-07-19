from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True




class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(BaseModel):
    title = models.CharField(max_length=150)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


