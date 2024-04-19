from django.contrib import admin
from .models import Sharer, SharerUpload, Like, Comment, Rating, SharerUploadFile, SharerUploadImage, SharerUploadVideo, TipBox, Dashboard
from django.db.models import Count, DecimalField, ExpressionWrapper, F, Avg
from django.utils.html import format_html
from .forms import SharerUploadForm

class SharerUploadFileInline(admin.TabularInline):
    model = SharerUploadFile
    extra = 1

class SharerUploadImageInline(admin.TabularInline):
    model = SharerUploadImage
    extra = 1

class SharerUploadVideoInline(admin.TabularInline):
    model = SharerUploadVideo
    extra = 1
    
@admin.register(Sharer)
class SharerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'username', 'email', 'category', 'is_sharer', 'average_rating', 'comment_count')  
    search_fields = ('id', 'name', 'username', 'email', 'category')     
    list_filter = ('category',)

    def average_rating(self, obj):
        avg_rating = Rating.objects.filter(sharer=obj).aggregate(avg_rating=Avg('rating'))['avg_rating']
        return avg_rating if avg_rating is not None else 0
    average_rating.short_description = 'Average Rating'

    def comment_count(self, obj):
        return Comment.objects.filter(post__uploaded_by=obj).count()
    comment_count.short_description = 'Comment Count'

@admin.register(SharerUpload)
class SharerUploadAdmin(admin.ModelAdmin):
    # form = SharerUploadForm
    list_display = ('id', 'title', 'uploaded_by', 'created_at', 'get_likes_count', 'get_unlikes_count', 'get_comments_count')  
    search_fields = ('id', 'title', 'uploaded_by__name') 
    list_filter = ('created_at', 'uploaded_by__category')
    inlines = [SharerUploadFileInline, SharerUploadImageInline, SharerUploadVideoInline]

    def get_likes_count(self, obj):
        return obj.likes.filter(liked=True).count()
    get_likes_count.short_description = 'Likes'

    def get_unlikes_count(self, obj):
        return obj.likes.filter(liked=False).count()
    get_unlikes_count.short_description = 'Unlikes'

    def get_comments_count(self, obj):
        return obj.comments.count()
    get_comments_count.short_description = 'Comments'

    def get_comments(self, obj):
        return '\n'.join([c.content for c in obj.comments.all()])
    get_comments.short_description = 'Comments'

    def get_likes(self, obj):
        return '\n'.join([f"{like.user.username} - Liked" if like.liked else f"{like.user.username} - Unliked" for like in obj.likes.all()])
    get_likes.short_description = 'Likes'

    def unlike_posts(self, request, queryset):
        for post in queryset:
            Like.objects.filter(post=post, liked=True).delete()
        self.message_user(request, "Selected posts unliked successfully.")
    unlike_posts.short_description = "Unlike selected posts"

    actions = ['unlike_posts']  # Registering the action within the SharerUploadAdmin class

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'liked', 'unliked')
    list_filter = ('liked', 'unliked')
    search_fields = ('user__username', 'post__title')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'profile_picture', 'post', 'comments', 'created_at')  
    search_fields = ('user__username', 'post__title', 'comments')  

    def profile_picture(self, obj):
        if obj.user.profile_picture:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(obj.user.profile_picture.url))
        else:
            return None

    profile_picture.short_description = 'Profile Picture'



class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'comment')
    search_fields = ('user__email', 'user__username')
    list_filter = ('rating',)



# Register your models here.
@admin.register(TipBox)
class TipBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'sharer', 'amount', 'timestamp', 'sender_username')
    search_fields = ('user__username', 'sharer__name')
    list_filter = ('timestamp',)

    def sender_username(self, obj):
        return obj.user.username

    sender_username.short_description = 'Sender Username'
    

@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('sharer', 'total_earnings')  
    search_fields = ('sharer__name',)



admin.site.register(Rating, RatingAdmin)