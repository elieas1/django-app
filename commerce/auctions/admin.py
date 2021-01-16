from django.contrib import admin
from .models import User,listing,Bidding,Watchlist,comment
# Register your models here.

admin.site.register(User)
admin.site.register(listing)
admin.site.register(Bidding)
admin.site.register(Watchlist)
admin.site.register(comment)