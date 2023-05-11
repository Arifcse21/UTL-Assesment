from django.contrib import admin
from user.models import User
# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        "username",
        "first_name",
        "last_name",
        "uuid",
        "is_superuser",
        "is_staff",
        "is_active"
    ]
    list_display_links = ['email', 'username', ]
