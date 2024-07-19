from django.contrib import admin
from .models import ContactMessage

# Register your models here.
class ContactMessageTable(admin.ModelAdmin):
    list_display=['id','college_name','phone','email','message']
admin.site.register(ContactMessage,ContactMessageTable)