from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'role', 'email', 'is_active')
    list_filter = ('is_active', 'role')
    search_fields = ('first_name', 'last_name', 'email') 