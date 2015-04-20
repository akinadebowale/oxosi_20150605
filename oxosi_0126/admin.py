from __future__ import unicode_literals

from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from .models import Block, BlockImage, BlockCategory


class BlockImageInline(TabularDynamicInlineAdmin):
    model = BlockImage

class BlockAdmin(PageAdmin):
    inlines = (BlockImageInline,)


admin.site.register(Block, BlockAdmin)
admin.site.register(BlockCategory)


"""

# minimal version

from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Block

admin.site.register(Block, PageAdmin)
admin.site.register(BlockCategory)

"""
