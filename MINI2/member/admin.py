from django.contrib import admin
from .models import Member

# Define the admin calss
class MemberAdmin(admin.ModelAdmin): #admin의 ModelAdmin 클래스 상속
    # pass #상속만 받아 새로운 클래스 생성
    list_display = ('user_name','user_pw','user_phone','c_date')

# Register the admin class with associated model
admin.site.register(Member, MemberAdmin)
