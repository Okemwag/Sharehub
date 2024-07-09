from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Post, LikePost


class LikePostInline(admin.TabularInline):
    model = LikePost
    extra = 0
    readonly_fields = ("user", "value")
    can_delete = False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "caption", "date_posted", "date_updated")
    list_filter = ("date_posted", "author")
    search_fields = (
        "author__username",
        "author__first_name",
        "author__last_name",
        "caption",
    )
    ordering = ("-date_posted",)
    readonly_fields = ("date_posted", "date_updated")
    inlines = [LikePostInline]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "author",
                    "caption",
                    "img",
                    "date_posted",
                    "date_updated",
                )
            },
        ),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ("author", "id")
        return self.readonly_fields


@admin.register(LikePost)
class LikePostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "value")
    list_filter = ("value", "user")
    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "post__caption",
    )
    ordering = ("-post__date_posted",)
    readonly_fields = ("user", "post", "value")

    fieldsets = ((None, {"fields": ("id", "user", "post", "value")}),)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ("user", "post")
        return self.readonly_fields
