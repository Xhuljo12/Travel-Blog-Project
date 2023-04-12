from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=100, null=True, blank=True)
    contact_surname = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_message = models.TextField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return f'{self.contact_name} {self.contact_surname}'


class Subscribe(models.Model):
    subscribe_id = models.AutoField(primary_key=True)
    subscribe_email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f'{self.subscribe_email}'

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, null=True, blank=True)
    category_image = models.FileField(upload_to="media/")
    category_description = models.TextField(max_length=10000, null=True, blank=True)

    def __str__(self):
        return f'{self.category_name}'


class Articles(models.Model):
    articles_id = models.AutoField(primary_key=True)
    articles_name = models.CharField(max_length=100, null=True, blank=True)
    articles_image = models.FileField(upload_to="media/")
    articles_description = models.TextField(max_length=10000, null=True, blank=True)
    articles_lines = models.TextField(max_length=10000, null=True, blank=True)
    articles_categories= models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.articles_name}'


class Comments(models.Model):
    comments_id = models.AutoField(primary_key=True)
    comments_email = models.EmailField(null=True, blank=True)
    comments_lines = models.TextField(max_length=1000, null=True, blank=True)
    comments_at = models.DateTimeField(auto_now_add=True)
    comments_categories= models.ForeignKey(Articles, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.comments_lines} {self.comments_email}'