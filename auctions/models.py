from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
    pass

class Watchlist(models.Model):
    user: models.ForeignKey(User, on_delete = models.CASCADE, related_name="comments_created")
    
    def __str(self):
        return f"{self.id}: {self.user}"
        
class Category(models.Model):
    name = models.CharField(max_length=128)
    def __str(self):
        return f"{self.id}: {self.name}"

class Listing (models.Model):
    STATES = (
    ('Act', 'Activo'),
    ('Inact', 'Inactivo'),)

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="auctions_created") #if user is deleted, auction will be deleted

    name = models.CharField(max_length=64)
    price = models.IntegerField() 
    create = models.DateField(auto_now_add=True, null=True, blank=True)
    descrpition=models.CharField(max_length=255,null=True)
    estate=models.CharField(max_length=8, choices=STATES, default='Act')
    image_url=models.CharField(max_length=128)
    category=models.ForeignKey(Category, on_delete = models.CASCADE, related_name="listing_cat_relation",null=True) #puede o no tener una lista asociada
    watchlist = models.ForeignKey(Watchlist, on_delete = models.CASCADE, related_name="listing_relation",blank=True,null=True) #puede o no tener una lista asociada
    
    def __str(self):
        return f"{self.id}: {self.name}, {self.create}"

class Bid(models.Model):

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="bids_created")
    listing =  models.ForeignKey(Listing, on_delete = models.CASCADE, related_name="bids_relation")

    value = models.IntegerField()
    def __str(self):
        return f"{self.id}: {self.user} {self.listing}, {self.value}"

class Comment (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name="comments_created")
    listing =  models.ForeignKey(Listing, on_delete = models.CASCADE, related_name="comments_relation")

    text = models.CharField(max_length=192)

    def __str(self):
        return f"{self.id}: {self.listing}, {self.text}"

