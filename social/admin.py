from django.contrib import admin
from social.models import Profile,Post,Comment,Like,FollowUser
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['status','Mobile_no','name']
    list_filter=('status',)
admin.site.register(Profile,ProfileAdmin),

class PostAdmin(admin.ModelAdmin):
    list_display=['Title','subject']
    search_fields=['Title']
    # list_filter=('flag',)

admin.site.register(Post,PostAdmin),

class CommentAdmin(admin.ModelAdmin):
    list_display=['post','msg']
    search_fields=['post']
    list_filter=('comment_by',)
admin.site.register(Comment,CommentAdmin),

class LikeAdmin(admin.ModelAdmin):
    list_display=['post','like_by']
    search_fields=['like_by']
    list_filter=('post',)
admin.site.register(Like,LikeAdmin),

class FollowUserAdmin(admin.ModelAdmin):
    list_display=['followe_by','create_date']
    list_filter=('create_date',)
admin.site.register(FollowUser,FollowUserAdmin)
