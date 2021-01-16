from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required
import re

from .models import User,listing,Bidding,Watchlist,comment

def index(request):
    return render(request, "auctions/index.html", {"list1":listing.objects.filter(active="True"),})

def item(request,id):
    if request.method == "POST":

        if not request.user.is_authenticated:
            return render(request, "auctions/login.html", {
                "message": "Only logged in users are allowed to bid."})
        elif request.POST.get("watch"):
            watch = request.POST.get("watch")
            list = listing.objects.get(id = id)
            add = Watchlist(user = request.user,listing_id= list)
            add.save()
            return HttpResponseRedirect(reverse("item",args={id}))

        elif request.POST.get("remove"):
            remove = request.POST.get("remove")
            delete = Watchlist.objects.filter(user = remove,listing_id=id).delete()
            return HttpResponseRedirect(reverse("item",args={id}))

        elif request.POST.get("close"):
            close = listing.objects.filter(id = id).update(active="False")
            return HttpResponseRedirect(reverse("item",args={id}))

        elif request.POST.get("save"):
            number = float(request.POST.get("bid"))
            list = listing.objects.filter(id = id).first()
            bids = Bidding.objects.filter(listing_id = id).order_by('-bid').first()
            if list.active == "False":
                return HttpResponseRedirect(reverse("item",args={id}))
            elif list.changed == "True" and number <= bids.bid:
                return HttpResponseRedirect(reverse("item",args={id}))
            else:
                add = Bidding(bid = number,date=datetime.now(),user = request.user ,listing_id=id)
                add.save()
                update = listing.objects.filter(id = id).update(bid = number,changed="True")
                return HttpResponseRedirect(reverse("item",args={id}))

        elif request.POST.get("savecomment"):
            text = request.POST.get("text")
            add = comment(user = request.user, listing_id = id,comments = text,date = datetime.now())
            add.save()
            return HttpResponseRedirect(reverse("item",args={id}))

        elif request.POST.get("delete"):
            delete = request.POST.get("delete")
            dele = comment.objects.filter(user = request.user,listing_id=id,comments = delete).delete()
            return HttpResponseRedirect(reverse("item",args={id}))

    else:
        bids = Bidding.objects.filter(listing_id = id).order_by('-bid').first()
        comments = comment.objects.filter(listing_id = id)
        bid = listing.objects.filter(id = id)
        for c in bid:
            bid = c.bid+0.01
            bid2 = c.bid
        return render(request, "auctions/item.html",
         {"id":id,"list":listing.objects.filter(id = id),"bid":bid,"bid2":bid2,
         "watchlist":Watchlist.objects.filter(listing_id = id,user = request.user),"comment":comments,
         "winner":Bidding.objects.filter(listing_id = id).order_by('-bid').first(),
         "bidders":Bidding.objects.filter(listing_id = id).order_by('-bid')})

def category(request):
    if request.method == "POST":
        categ = request.POST.get("select")
        return render(request, "auctions/category.html", {"categ":listing.objects.filter(category__contains = categ,active = "True"),
        "cat":listing.objects.values('category').distinct(),"cate":categ})
    return render(request, "auctions/category.html")
    
@login_required
def watchlist(request):
    data = Watchlist.objects.filter(user = request.user) \
                   .values('listing_id__title', 'listing_id__category','listing_id__image',
                   'listing_id__by','listing_id__date','listing_id__description','listing_id__id','listing_id__bid','listing_id__active')
    return render(request,"auctions/watch.html",{"categ":data})

@login_required
def myitems(request):
    data = listing.objects.filter(by = request.user)
    return render(request,"auctions/myitems.html",{"categ":data})

def create(request):
    if not request.user.is_authenticated:
        return render(request, "auctions/login.html", {
                "message": "You should be logged in to view requested page."})
    else:
        if request.method == "POST":
            title = request.POST.get("title")
            bid = request.POST.get("bid")
            url = request.POST.get("url")
            cat = str(request.POST.getlist("cat"))
            desc = request.POST.get("desc")
            by = request.POST.get("user")

            cat = re.sub("\[|'|\]", "", cat)

            add = listing(title = title,description = desc, bid = bid, image =url, category = cat,
             date = datetime.now(),by=by)
            add.save()
            return HttpResponseRedirect(reverse("index"))
        
        else:
            return render(request, "auctions/create.html")


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
