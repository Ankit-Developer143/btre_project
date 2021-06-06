from django.contrib import admin

from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    
    # List Display Link admin panel
    list_display_links = ('id','title')
    
    # filter by title
    list_filter = ('realtor',)
    
    # editable
    list_editable = ('is_published',)
    
    #search
    search_fields = ('title','description','address','city','state','zipcode','price',)
    
    #list per page
    list_per_page = 25
admin.site.register(Listing,ListingAdmin)
