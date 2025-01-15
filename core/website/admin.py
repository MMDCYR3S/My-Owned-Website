from django.contrib import admin
from .models import Contact

# Register contact admin panel
@admin.register(Contact)
class ContactAdminPanel(admin.ModelAdmin):
    list_display = ("email", "created_date")
    list_filter = ("email",)
    search_fields = ("email", "message")
    