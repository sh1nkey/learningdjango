from django.contrib import admin

# Register your models here.
from users.models import User
from products.admin import BasketAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    in_lines =  (BasketAdmin, )


