from django.db import models
from django.template.defaultfilters import slugify



class Forum(models.Model):

    title = models.CharField(max_length=45)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='forum_images', null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class Thread(models.Model):
    title = models.CharField(max_length=45)
    slug = models.SlugField(max_length=60, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


class Message(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    ban = models.BooleanField(default=False)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Message {self.created_at.strftime('%H:%M:%S')}"


