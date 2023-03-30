from django.db import models
from django.contrib.auth import get_user_model
from crum import get_current_user
User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

class Content(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(blank=True, upload_to='document')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.user = user
        super(Content, self).save(*args, **kwargs)
    