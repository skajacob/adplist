from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username','pk', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'rating', 'reviews_count', 'first_name', 'last_name', "location", 'employer', 'user_type', 'title',)
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, AccountAdmin)