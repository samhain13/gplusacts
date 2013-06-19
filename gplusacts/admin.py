from django.contrib import admin
from gplusacts.models import Activity, Attachment

class AttachmentInline(admin.StackedInline):
    model = Attachment
    extra = 1


class ActivityAdmin(admin.ModelAdmin):
    list_display = ["objtype", "content", "url"]
    search_fields = ["objtype", "content"]
    date_hierarchy = "published"
    inlines = [AttachmentInline]

admin.site.register(Activity, ActivityAdmin)
