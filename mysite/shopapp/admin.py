from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from  .models import Product, Order
# from  shopapp.admin_mixins import ExportAsCSVMixin


# admin.site.register(Product)

class OrderInline(admin.TabularInline):
    model = Product.orders.through


@admin.action(description='Archive Products')
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_archived=True)


@admin.action(description='Unarchive Products')
def mark_unarchived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(is_archived=False)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = [
        mark_archived,
        mark_unarchived,
        'export_csv'
    ]
    inlines = [
        OrderInline,
    ]
    list_display = 'pk', 'name', 'description_short','price','created_at','is_archived','color','preview'
    list_display_links = 'pk', 'name'
    ordering = '-name', 'pk'
    search_fields = 'name','color','preview'
    fieldsets = [
        (None, {
            'fields': ('name', 'description'),
        }),
        ('Color options',{
            'fields':('color',),
            'classes': ('collapse',)
        }),
        ('Picture options',{
            'fields':('preview',),
            'classes': ('collapse',)
        }),
        ('Price options', {
            'fields': ('price', 'discount'),
            'classes': ('collapse', 'wide')
        }),
        ('Extra options', {
            'fields': ('is_archived',),
            'classes': ('collapse',),
            'description': 'Extra options. Field "archived" is for soft delete',
        })
    ]

    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'


# class ProductInline(admin.TabularInline):
class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]
    list_display = 'pk', 'delivery_address', 'promocode', 'user_verbose', 'created_at'

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')

    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username