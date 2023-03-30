from django.contrib import admin
from core.models import User
from django.contrib.auth.admin import UserAdmin
from core.forms import UserForm,CustomUserChangeForm



class CustomUserAdmin(UserAdmin):
    form =CustomUserChangeForm
    add_form = UserForm
    model = User
    add_fieldsets=(
    ('Personal Detail', {'fields':('username','full_name','email','password','phone_number','address', 'state', 'city', 'country','pincode')}),
    ('Permissions', {'fields':('is_staff','is_active')})
    )
    fieldsets=(
    ('Personal Detail', {'fields':('username','full_name','email','password','phone_number','address', 'state', 'city', 'country','pincode')}),
    ('Permissions', {'fields':('is_staff','is_active')})
    )
    list_display = ( 'email','full_name','phone_number', 'pincode','is_superuser')

admin.site.register(User, CustomUserAdmin)