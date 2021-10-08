from django.contrib import admin
from .models import Thebig5, Sublink, BT, BTone, BTtwo, BTthree, Post, BTOnePost, BTTwoPost, BTThreePost, Community, SublinkCommunity, Learning, SublinkLearning, Technology, SublinkTechnology
# , Big5name, Big5s
# Register your models here.
admin.site.register(Thebig5)
admin.site.register(Sublink)
admin.site.register(BT)
admin.site.register(BTone)
admin.site.register(BTtwo)
admin.site.register(BTthree)
admin.site.register(BTOnePost)
admin.site.register(BTTwoPost)
admin.site.register(BTThreePost)
admin.site.register(Community)
admin.site.register(SublinkCommunity)
admin.site.register(Learning)
admin.site.register(SublinkLearning)
admin.site.register(Technology)
admin.site.register(SublinkTechnology)

# admin.site.register(Big5name)
# admin.site.register(Big5s)