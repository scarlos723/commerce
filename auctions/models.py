from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing (models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="auctions_created") #if user is deleted, auction will be deleted

    name = models.CharField(max_length=64)
    price = models.IntegerField() 
    create = models.CharField(max_length=64)
    image_url=models.CharField(max_length=128)
    def __str(self):
        return f"{self.id}: {self.name}, {self.create}"

class Bidding (models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="biddings_created")
    listing =  models.ForeignKey(Listing, on_delete = models.CASCADE, related_name="biddings_relation")

    value = models.IntegerField()
    def __str(self):
        return f"{self.id}:  {self.listing}, {self.value}"

class Comment (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="comments_created")
    listing =  models.ForeignKey(Listing, on_delete = models.CASCADE, related_name="comments_relation")

    text = models.CharField(max_length=192)

    def __str(self):
        return f"{self.id}: {self.listing}, {self.text}"