from django.contrib import admin
from poll.models import *
from hvad.admin import TranslatableAdmin, TranslatableTabularInline


class PollItemInline(TranslatableTabularInline):
    model = Item
    extra = 0
    max_num = 15
    list_display = ['pos', ]


class PollAdmin(TranslatableAdmin):
    inlines = [PollItemInline, ]


class ItemAdmin(TranslatableAdmin):
    pass

admin.site.register(Item, ItemAdmin)
admin.site.register(Poll, PollAdmin)
