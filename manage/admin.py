from django.contrib import admin
from manage.models import Maintenance,Notice,Applist, UpdateList
from form import NoticeForm, UpdateForm

class NoticeAdmin(admin.ModelAdmin):
    form = NoticeForm

class UpdateAdmin(admin.ModelAdmin):
    form = UpdateForm

admin.site.register(Maintenance)
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Applist)
admin.site.register(UpdateList, UpdateAdmin)
# Register your models here.
