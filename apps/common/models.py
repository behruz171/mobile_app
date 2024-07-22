from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Content(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes", blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="content")
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)

    def __str__(self):
        return self.title


class Episode(BaseModel):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='episodes')
    movie = models.FileField(upload_to="content_files/")
    title = models.CharField(max_length=255)
    episode_number = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('content', 'episode_number')

    def __str__(self):
        return f"{self.content.title} - Episode {self.episode_number}"
