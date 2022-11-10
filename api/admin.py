from django.contrib import admin
from rest_framework.authtoken.models import Token
from api.models import UserProfile, Task, FieldTeam, PromotionTeam,Team,TeamUsers,Question,Media,MediaBrief,Campaign



class UserProfileAdmin(admin.ModelAdmin):
    #search_fields = ['name','image','social_auth_type','social_auth_code','phone','location','facebook','instagram','twitter','paypal','created_by','created_date','modified_by','modified_date','is_enabled']
    search_fields = ['name','image','location']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Task)
admin.site.register(FieldTeam)
admin.site.register(Team)
admin.site.register(TeamUsers)
admin.site.register(Question)
admin.site.register(Media)
admin.site.register(MediaBrief)
admin.site.register(Campaign)