from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Listing,User,Category, Bid,Comment


def index(request):
    listings= Listing.objects.all()
    return render(request, "auctions/index.html", {"listings": listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def show_list(request, id):
    listing= Listing.objects.get( pk = id )
    comments=Comment.objects.filter(listing=id)
    
    return render(request, "auctions/listing.html", {"listing": listing, "comments":comments})

def show_categories(request):
    categories=Category.objects.all()
    return render(request, "auctions/categories.html",{"categories":categories})

def create_list(request):
    if request.method=="POST":
        
        name_html = request.POST["name"]
        price = int(request.POST["price"])
        descrpition=request.POST["description"]
        image_url=request.POST["image_url"]
        cat = request.POST["category"]
        print(f"esta es la request {cat}")
        category = Category.objects.get(pk=request.POST["category"])

        user = User.objects.get(pk=request.POST["user"])

        listing = Listing.objects.create(user=user, name=name_html, price=price, descrpition=descrpition, image_url=image_url, category=category)
        listing.save()
        return render(request,"auctions/listing.html",{"listing":listing, "alert":"List create"})

    categories=Category.objects.all()
    return render(request,"auctions/create_listing.html",{"categories":categories})

def create_bid(request,id):
    if request.method == "POST":
        
        listing=Listing.objects.get(pk=id)
        value_bid=int(request.POST["bid"])
        
        if value_bid >= listing.price:
            user = User.objects.get(pk=request.POST["user"])
            listing.price=value_bid
            listing.save()
            bid=Bid.objects.create(user=user,listing=listing,value=value_bid)
            bid.save()
            
            return render(request,"auctions/listing.html",{"listing":listing, "alert":"The Bid has been create"})
        else:
            return render(request,"auctions/listing.html",{"listing":listing, "alert":"The Bid values must be major that actual price "})

    return HttpResponseRedirect(reverse("index"))

def create_comment(request,id):

    if request.method == "POST":
        
        listing=Listing.objects.get(pk=id)
        text_comment=request.POST["comment"]
          
        user = User.objects.get(pk=request.POST["user"])
        
        comment=Comment.objects.create(user=user,listing=listing,text=text_comment)
        comment.save()
        
        return render(request,"auctions/listing.html",{"listing":listing, "alert":"The Comment has been create"})
    
       

    return HttpResponseRedirect(reverse("index"))

def show_category(request, id):
    listings = Listing.objects.filter(category=id)
    return render(request,"auctions/list_categories.html",{"listings":listings})


def show_watchlist(request,id):
    bids = Bid.objects.filter(user=id)
    return render(request,"auctions/watchlist.html",{"bids":bids})

def edit_list(request, id):

    if request.method == "POST":
        listing = Listing.objects.get(pk=id)
        if listing.estate == 'Act':
            listing.estate = 'Inact'
        else:
            listing.estate = 'Act'

        listing.save()
        comments=Comment.objects.filter(listing=id)
    
        return render(request, "auctions/listing.html", {"listing": listing, "comments":comments})
    
    return HttpResponseRedirect(reverse("index"))