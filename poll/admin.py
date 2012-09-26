from django.contrib import admin
from poll.models import *
from django.utils.translation import gettext as _
from hvad.admin import TranslatableAdmin

class PollItemInline(admin.TabularInline):
    model = Item
    extra = 0
    max_num = 15

class PollAdmin(TranslatableAdmin):
    #list_display = ('title', 'date', 'vote_count', 'is_published')
    #inlines = [PollItemInline,]
    pass

class ItemAdmin(TranslatableAdmin):
	pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Poll, PollAdmin)


# class VoteAdmin(admin.ModelAdmin):
#     list_display = ('poll', 'ip', 'user', 'datetime')
#     list_filter = ('poll', 'datetime')
# 
# admin.site.register(Vote, VoteAdmin)
