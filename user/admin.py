


from django.contrib import admin
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


#user info 에 profile 같이보기 stacked 세로 tabula 가로 
class UserProfileInline(admin.StackedInline):
    model = UserProfileModel

    # 추가로 취미도 세팅가능
    # filter_horizontal = ['hobby']

class UserAdmin(BaseUserAdmin):


    list_display = ('id', 'username', 'fullname', 'email')
    list_display_links = ('username', )
    list_filter = ('username', )
    search_fields = ('username', 'email', )

    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date', )}),
        ('Permissions', {'fields': ('is_admin', 'is_active', )}),
    )
    inlines = (UserProfileInline, )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'fullname', 'password1', 'password2')}
        ),
    )
    

    filter_horizontal = []

    def get_readonly_fields(self, request, obj: None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )

    



# Register your models here.
admin.site.register(UserModel, UserAdmin)
admin.site.register(UserProfileModel)