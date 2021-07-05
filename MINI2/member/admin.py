from django.contrib import admin
from .models import Member, Profile

# Define the admin calss
class MemberAdmin(admin.ModelAdmin): #admin의 ModelAdmin 클래스 상속
    # pass #상속만 받아 새로운 클래스 생성
    list_display = ('user_name','user_pw','user_phone','c_date')

# Register the admin class with associated model
admin.site.register(Member, MemberAdmin)

### 추가된부분 ###
# 프로필 
class ProfileAdmin(admin.StackedInline):
    model = Profile
    con_delete = False

class CustomUserAdmin(MemberAdmin):
    inlines = (ProfileAdmin,)

admin.site.unregister(Member)
admin.site.register(Member, CustomUserAdmin)
