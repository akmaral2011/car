from django.contrib import admin
from.models import Car

class PersonAdmin(admin.ModelAdmin):
    list_display = ['model','price','land','color','description',]
    list_filter = ['model','price','color',]
    search_fields = ['model']


admin.site.register(Car)


