from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=17)
    content = models.TextField()
    
    def __str__(self):
        return self.name

class Post(models.Model):
    CATEGORY = (('Teacher', 'Teacher'), ('Student', 'Student'))
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=101)
    slug = models.CharField(max_length=100, default=title)
    email = models.EmailField()
    salary = models.FloatField()
    details = models.TextField()
    available = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    created_at = models.DateTimeField(default=now)
    image = models.ImageField(default="default.png", upload_to="tuition/images")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.width > 300 or img.height > 300:
            output_size = [300, 300]
            img.thumbnail(output_size)
            img.save(self.image.path)
        