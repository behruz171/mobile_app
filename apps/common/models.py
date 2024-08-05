from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Content(BaseModel):
    CONTENT_TYPE_CHOICES = (
        ('movie', 'Movie'),
        ('serial', 'Serial'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    poster = models.ImageField(upload_to="images/", blank=True, null=True)
    release_date = models.DateField()
    categories = models.ManyToManyField(Category)
    duration = models.PositiveIntegerField(help_text="Duration in minutes", blank=True, null=True)
    content_type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES)

    def __str__(self):
        return self.title


class Episode(BaseModel):
    content = models.ForeignKey(Content, related_name='episodes', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    episode_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.content.title} - Episode {self.episode_number}: {self.title}"


class Qism(BaseModel):
    episode = models.ForeignKey(Episode, related_name='qismlar', on_delete=models.CASCADE)
    qism_number = models.PositiveIntegerField()
    movie = models.FileField(upload_to='movies/')

    def __str__(self):
        return f"Qism {self.qism_number} - {self.episode.title}"



class Questions(BaseModel):
    question = models.TextField()
    answer = models.CharField(max_length=100)
    