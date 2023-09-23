from django.contrib import admin
from .models import TimeTrackinEntry


class YourModelAdmin(admin.ModelAdmin):
    list_display = (
        "datetime_col",
        "last_update",
    )


admin.site.register(TimeTrackinEntry, YourModelAdmin)
# from django.contrib import admin
# from .models import YourModel


# class YourModelAdmin(admin.ModelAdmin):
#     list_display = ("datetime_col", "datetime_col_UTC", "datetime_col_PST")


# admin.site.register(YourModel, YourModelAdmin)
