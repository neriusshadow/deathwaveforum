from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_banned', 'ban_reason', 'last_seen')
    list_filter = ('is_banned',)
    search_fields = ('user__username', 'ban_reason')
    fields = ('user', 'is_banned', 'ban_reason', 'avatar', 'bio', 'location', 'birth_date', 'reputation', 'is_online', 'last_seen', 'ip_address')
    readonly_fields = ('reputation', 'is_online', 'last_seen', 'ip_address')

admin.site.register(Profile, ProfileAdmin)
