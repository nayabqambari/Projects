from django.contrib import admin

# Register your models here.


from .models import ContactUs 

class ContactUsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Contact Information', {'fields': ['name', 'email', 'subject', 'message']}),
    ]


admin.site.register(ContactUs, ContactUsAdmin)