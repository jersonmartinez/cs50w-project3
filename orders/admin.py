from django.contrib import admin
from .models import MenuItem, Topping, OrderItem, Order, Extra


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'user', 'total', 'items']
    list_filter = ['status']

    def items(self, obj):
        value = ""
        for orderitem in obj.orderitem_set.all():
            value += f"\n {orderitem}"

        return value


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(MenuItem)
admin.site.register(Topping)
admin.site.register(Extra)
