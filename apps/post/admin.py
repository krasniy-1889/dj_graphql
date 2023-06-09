from django.contrib import admin

from apps.post.models import Post, Comment


# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "like_count",
        "view_count",
        "created_at",
        "updated_at",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["content", "is_active", "created_at", "updated_at"]
    list_filter = ["is_active"]
    actions = ["approve_comment", "inactive_comment"]

    def approve_comment(self, request, queryset):
        queryset.update(is_active=True)

    def inactive_comment(self, request, queryset):
        queryset.update(is_active=False)

    approve_comment.short_description = "Approve selected comments"
    inactive_comment.short_description = "Inactive selected comments"
