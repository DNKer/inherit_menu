from django.contrib import admin

from menu.models import Item, Menu


class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'parent',
        'menu',
        'url'
    )
    list_filter = (
        'menu',
        'parent'
    )
    prepopulated_fields = {
        'url': ('title',)
    }

    def save_model(self, request, obj, form, change) -> None:
        """
        Метод для формирования `url` в админ панели.
        """
        obj.url = (
            f'/{obj.menu.title}/{obj.url}/'
        )
        obj.save()


admin.site.register(Item, MenuItemAdmin)
admin.site.register(Menu)
